import json
from pathlib import Path

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from skill_normalizer import normalize_skills_text

DATA_PATH = Path(__file__).with_name("dataset.csv")
ARTIFACT_DIR = Path(__file__).with_name("model_artifacts")
ARTIFACT_PATH = ARTIFACT_DIR / "career_model.joblib"
METRICS_PATH = ARTIFACT_DIR / "metrics.json"


def train_and_save(dataset_path=DATA_PATH):
    data = pd.read_csv(dataset_path)
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
    metrics = {
        "accuracy": float(accuracy_score(y_test, preds)),
        "f1_macro": float(f1_score(y_test, preds, average="macro")),
        "f1_weighted": float(f1_score(y_test, preds, average="weighted")),
        "support": int(len(y_test)),
    }

    ARTIFACT_DIR.mkdir(exist_ok=True)
    joblib.dump(
        {
            "model": model,
            "vectorizer": vectorizer,
            "encoder": encoder,
            "metrics": metrics,
        },
        ARTIFACT_PATH,
    )
    METRICS_PATH.write_text(json.dumps(metrics, indent=2))

    return metrics


if __name__ == "__main__":
    results = train_and_save()
    print("Training complete. Metrics:")
    print(json.dumps(results, indent=2))
