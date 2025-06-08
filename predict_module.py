"""Prediction utilities for horse racing."""

from pathlib import Path
from typing import Dict

import joblib
import pandas as pd

_MODEL_PATH = Path("race_model.joblib")
_ENCODER_PATHS: Dict[str, Path] = {
    "course": Path("le_course.joblib"),
    "going": Path("le_going.joblib"),
    "jockey": Path("le_jockey.joblib"),
    "trainer": Path("le_trainer.joblib"),
    "type": Path("le_type.joblib"),
}


def _load_encoders() -> Dict[str, object]:
    """Load label encoders from disk if the files exist."""
    return {
        name: joblib.load(path)
        for name, path in _ENCODER_PATHS.items()
        if path.exists()
    }


def _load_model():
    if not _MODEL_PATH.exists():
        raise FileNotFoundError(f"Model file not found: {_MODEL_PATH}")
    return joblib.load(_MODEL_PATH)


_encoders = _load_encoders()
try:
    _model = _load_model()
except FileNotFoundError:
    _model = None


def _encode_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    if "jockey" in df and "jockey" in _encoders:
        df["jockey_enc"] = _encoders["jockey"].transform(df["jockey"].fillna("Unknown"))
    if "trainer" in df and "trainer" in _encoders:
        df["trainer_enc"] = _encoders["trainer"].transform(df["trainer"].fillna("Unknown"))
    if "course" in df and "course" in _encoders:
        df["course_enc"] = _encoders["course"].transform(df["course"].fillna("Unknown"))
    if "going" in df and "going" in _encoders:
        df["going_enc"] = _encoders["going"].transform(df["going"].fillna("Unknown"))
    if "type" in df and "type" in _encoders:
        df["type_enc"] = _encoders["type"].transform(df["type"].fillna("Unknown"))
    df["draw"] = pd.to_numeric(df.get("draw", 0), errors="coerce").fillna(0)
    return df


def encode_and_predict(df: pd.DataFrame) -> pd.DataFrame:
    """Return predictions sorted by win probability."""
    if _model is None:
        raise FileNotFoundError(f"Model file not found: {_MODEL_PATH}")

    df = _encode_features(df)
    feature_cols = [
        "draw",
        "jockey_enc",
        "trainer_enc",
        "course_enc",
        "going_enc",
        "type_enc",
    ]
    X = df[feature_cols]
    win_prob = _model.predict_proba(X)[:, 1]
    df = df.copy()
    df["win_probability"] = win_prob
    return df.sort_values("win_probability", ascending=False)
