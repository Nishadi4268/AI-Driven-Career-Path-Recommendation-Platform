from pathlib import Path

import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier

from skill_normalizer import normalize_skills_text

DATA_PATH = Path(__file__).with_name("dataset.csv")
ARTIFACT_DIR = Path(__file__).with_name("model_artifacts")
ARTIFACT_PATH = ARTIFACT_DIR / "career_model.joblib"


def _train_from_dataset():
    data = pd.read_csv(DATA_PATH)
    data["skills"] = data["skills"].fillna("").apply(normalize_skills_text)
    data["interest"] = data["interest"].fillna("")
    data["education"] = data["education"].fillna("")

    X = data["skills"] + " " + data["interest"] + " " + data["education"]
    y = data["career"]

    vectorizer = TfidfVectorizer(
        lowercase=True,
        ngram_range=(1, 2),
        max_features=500,
        min_df=1
    )
    X_vec = vectorizer.fit_transform(X)

    encoder = LabelEncoder()
    y_enc = encoder.fit_transform(y)

    model = RandomForestClassifier(
        n_estimators=200,
        max_depth=20,
        min_samples_split=2,
        random_state=42,
        class_weight="balanced"
    )
    model.fit(X_vec, y_enc)
    return model, vectorizer, encoder, None


def _load_or_train_model():
    if ARTIFACT_PATH.exists():
        artifacts = joblib.load(ARTIFACT_PATH)
        return (
            artifacts["model"],
            artifacts["vectorizer"],
            artifacts["encoder"],
            artifacts.get("metrics"),
        )

    return _train_from_dataset()


model, vectorizer, encoder, MODEL_METRICS = _load_or_train_model()

# Prediction function
def predict_career(skills, interest, education):
    skills_clean = normalize_skills_text(skills)
    text = f"{skills_clean} {interest} {education}".strip()
    vec = vectorizer.transform([text])

    pred = model.predict(vec)
    proba = model.predict_proba(vec)

    career = encoder.inverse_transform(pred)[0]
    confidence = float(proba.max())

    return career, confidence


def get_model_metrics():
    return MODEL_METRICS
