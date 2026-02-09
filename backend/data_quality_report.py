import json
from pathlib import Path

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from skill_normalizer import normalize_skills_text

BASE_DIR = Path(__file__).parent
DATASET_PATH = BASE_DIR / "dataset.csv"
REPORT_PATH = BASE_DIR / "data_quality_report.json"


def generate_report():
    data = pd.read_csv(DATASET_PATH)

    duplicate_mask = data.duplicated(subset=["skills", "interest", "education", "career"])
    duplicate_count = int(duplicate_mask.sum())

    career_counts = data["career"].value_counts()
    imbalance_ratio = None
    if not career_counts.empty:
        imbalance_ratio = float(career_counts.max() / career_counts.min())

    data["skills"] = data["skills"].fillna("").apply(normalize_skills_text)
    data["interest"] = data["interest"].fillna("")
    data["education"] = data["education"].fillna("")

    X = data["skills"] + " " + data["interest"] + " " + data["education"]
    y = data["career"]

    vectorizer = TfidfVectorizer(
        lowercase=True,
        ngram_range=(1, 2),
        max_features=500,
        min_df=1,
    )
    X_vec = vectorizer.fit_transform(X)

    encoder = LabelEncoder()
    y_enc = encoder.fit_transform(y)

    X_train, X_test, y_train, y_test = train_test_split(
        X_vec,
        y_enc,
        test_size=0.2,
        random_state=42,
        stratify=y_enc,
    )

    model = RandomForestClassifier(
        n_estimators=200,
        max_depth=20,
        min_samples_split=2,
        random_state=42,
        class_weight="balanced",
    )
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    label_ids = sorted(set(y_test))
    label_names = encoder.inverse_transform(label_ids)
    report_dict = classification_report(
        y_test,
        preds,
        labels=label_ids,
        target_names=label_names,
        output_dict=True,
        zero_division=0,
    )

    per_career = {
        label: {
            "precision": report_dict[label]["precision"],
            "recall": report_dict[label]["recall"],
            "f1": report_dict[label]["f1-score"],
            "support": report_dict[label]["support"],
        }
        for label in label_names
        if label in report_dict
    }

    report = {
        "total_rows": int(len(data)),
        "duplicate_rows": duplicate_count,
        "career_counts": career_counts.to_dict(),
        "min_class_size": int(career_counts.min()) if not career_counts.empty else 0,
        "max_class_size": int(career_counts.max()) if not career_counts.empty else 0,
        "imbalance_ratio": imbalance_ratio,
        "per_career_metrics": per_career,
        "overall_metrics": {
            "accuracy": report_dict.get("accuracy"),
            "macro_avg": report_dict.get("macro avg"),
            "weighted_avg": report_dict.get("weighted avg"),
        },
    }

    REPORT_PATH.write_text(json.dumps(report, indent=2))
    return report


if __name__ == "__main__":
    results = generate_report()
    print(json.dumps(results, indent=2))
