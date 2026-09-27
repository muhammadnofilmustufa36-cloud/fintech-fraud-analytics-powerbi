"""Memory-conscious ETL and Isolation Forest scoring for the fraud CSV."""
from __future__ import annotations

import gc
import time
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler


SOURCE = Path("financial_fraud_detection_dataset.csv")
OUTPUT = Path("processed_financial_fraud_data.csv")
CHUNK_SIZE = 50_000
MEDIAN_SAMPLE_PER_CHUNK = 2_000
MODEL_SAMPLE_SIZE = 100_000
RANDOM_SEED = 42
FEATURES = [
    "amount",
    "spending_deviation_score",
    "velocity_score",
    "geo_anomaly_score",
    "time_since_last_transaction",
]


def numeric_matrix(chunk: pd.DataFrame, medians: pd.Series | None = None) -> pd.DataFrame:
    """Coerce selected fields to numeric and use the fitted medians for true nulls."""
    result = chunk.loc[:, FEATURES].apply(pd.to_numeric, errors="coerce")
    result = result.replace([np.inf, -np.inf], np.nan)
    if medians is not None:
        result = result.fillna(medians).fillna(0.0)
    return result.astype(np.float32)


def main() -> None:
    started = time.perf_counter()
    if not SOURCE.is_file():
        raise FileNotFoundError(f"Input file not found: {SOURCE.resolve()}")

    columns = pd.read_csv(SOURCE, nrows=0).columns.tolist()
    missing = sorted(set(FEATURES + ["fraud_type"]) - set(columns))
    if missing:
        raise ValueError(f"Input is missing required columns: {missing}")

    # Pass 1: retain a reproducible, bounded sample for robust median estimates
    # and for Isolation Forest training. This avoids ever loading all 5M rows.
    rng = np.random.default_rng(RANDOM_SEED)
    sampled_parts: list[np.ndarray] = []
    rows_seen = 0
    for chunk in pd.read_csv(SOURCE, usecols=FEATURES, chunksize=CHUNK_SIZE):
        values = numeric_matrix(chunk).to_numpy()
        take = min(MEDIAN_SAMPLE_PER_CHUNK, len(values))
        sampled_parts.append(values[rng.choice(len(values), size=take, replace=False)])
        rows_seen += len(chunk)
        print(f"Median/training sample pass: {rows_seen:,} rows", flush=True)

    sample = np.vstack(sampled_parts)
    medians = pd.Series(np.nanmedian(sample, axis=0), index=FEATURES).fillna(0.0)
    # NaNs in the bounded sample are now imputed using its per-feature median.
    sample = np.where(np.isfinite(sample), sample, medians.to_numpy(dtype=np.float32))
    if len(sample) > MODEL_SAMPLE_SIZE:
        sample = sample[rng.choice(len(sample), size=MODEL_SAMPLE_SIZE, replace=False)]
    del sampled_parts
    gc.collect()

    # Pass 2: fit scaler over every cleaned row, using partial_fit to cap memory.
    scaler = StandardScaler()
    rows_seen = 0
    for chunk in pd.read_csv(SOURCE, usecols=FEATURES, chunksize=CHUNK_SIZE):
        scaler.partial_fit(numeric_matrix(chunk, medians))
        rows_seen += len(chunk)
        print(f"Scaler pass: {rows_seen:,} rows", flush=True)

    training_data = scaler.transform(sample)
    model = IsolationForest(
        n_estimators=150,
        max_samples="auto",
        contamination="auto",
        random_state=RANDOM_SEED,
        n_jobs=-1,
    )
    model.fit(training_data)

    # Calibrate raw anomaly scores to a bounded 0--100 scale using the training
    # sample's observed score range. Higher values mean more anomalous.
    calibration_scores = -model.decision_function(training_data)
    score_low, score_high = np.percentile(calibration_scores, [0.5, 99.5])
    if score_high <= score_low:
        score_high = score_low + 1.0
    del training_data, sample, calibration_scores
    gc.collect()

    # Pass 3: clean, score, append requested fields, and stream the full export.
    if OUTPUT.exists():
        OUTPUT.unlink()
    rows_seen = 0
    high_risk_count = 0
    first_chunk = True
    for chunk in pd.read_csv(SOURCE, chunksize=CHUNK_SIZE):
        # Blank strings and parser NaNs are both normalized to the requested label.
        fraud_text = chunk["fraud_type"].astype("string").str.strip()
        chunk["fraud_type"] = fraud_text.mask(fraud_text.isna() | fraud_text.eq(""), "Legitimate / Non-Fraud")

        clean_features = numeric_matrix(chunk, medians)
        # Persist typed / imputed numeric fields in the output as well.
        # Assign columns individually so pandas can safely promote originally
        # integer-typed fields when median imputation produces decimals.
        for feature in FEATURES:
            chunk[feature] = clean_features[feature].to_numpy()
        raw_anomaly = -model.decision_function(scaler.transform(clean_features))
        probability = np.clip((raw_anomaly - score_low) * 100.0 / (score_high - score_low), 0.0, 100.0)
        chunk["Fraud_Probability_%"] = np.round(probability, 2)
        chunk["Risk_Category"] = np.where(probability >= 65.0, "High Risk", "Normal")
        high_risk_count += int((probability >= 65.0).sum())
        chunk.to_csv(OUTPUT, mode="w" if first_chunk else "a", header=first_chunk, index=False)
        first_chunk = False
        rows_seen += len(chunk)
        print(f"Export/scoring pass: {rows_seen:,} rows", flush=True)

    elapsed = time.perf_counter() - started
    print("\nPipeline complete")
    print(f"Total Rows Processed: {rows_seen:,}")
    print(f"Total High Risk Count: {high_risk_count:,}")
    print(f"Execution Time: {elapsed:.2f} seconds")
    print(f"Output: {OUTPUT.resolve()}")


if __name__ == "__main__":
    main()
