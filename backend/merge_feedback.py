from pathlib import Path

import pandas as pd

from skill_normalizer import normalize_skills_text
from train_model import train_and_save

BASE_DIR = Path(__file__).parent
DATASET_PATH = BASE_DIR / "dataset.csv"
FEEDBACK_PATH = BASE_DIR / "feedback.csv"
OUTPUT_PATH = BASE_DIR / "dataset_merged.csv"


def _pick_career(row):
    selected = str(row.get("selected_career", "")).strip()
    if selected:
        return selected

    helpful = str(row.get("helpful", "")).strip().lower()
    if helpful == "true":
        return str(row.get("recommended_career", "")).strip()

    return ""


def merge_feedback(auto_retrain=True):
    if not FEEDBACK_PATH.exists():
        raise FileNotFoundError("feedback.csv not found. Collect feedback first.")

    dataset = pd.read_csv(DATASET_PATH)
    feedback = pd.read_csv(FEEDBACK_PATH)

    feedback["career"] = feedback.apply(_pick_career, axis=1)
    feedback = feedback[feedback["career"].astype(str).str.strip().ne("")]

    feedback["skills"] = feedback["skills"].fillna("").apply(normalize_skills_text)
    feedback["interest"] = feedback["interest"].fillna("")
    feedback["education"] = feedback["education"].fillna("")

    feedback_rows = feedback[["skills", "interest", "education", "career"]]

    merged = pd.concat([dataset, feedback_rows], ignore_index=True)
    merged = merged.drop_duplicates(
        subset=["skills", "interest", "education", "career"],
        keep="last",
    )

    merged.to_csv(OUTPUT_PATH, index=False)

    metrics = None
    if auto_retrain:
        metrics = train_and_save(dataset_path=OUTPUT_PATH)

    return OUTPUT_PATH, metrics


if __name__ == "__main__":
    path, metrics = merge_feedback()
    print(f"Merged dataset saved to: {path}")
    if metrics:
        print("Retraining complete. Metrics:")
        print(metrics)
