import csv
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).parent
FEEDBACK_PATH = BASE_DIR / "feedback.csv"

FIELDNAMES = [
    "timestamp",
    "skills",
    "interest",
    "education",
    "recommended_career",
    "selected_career",
    "helpful",
    "comment",
]


def store_feedback(record):
    FEEDBACK_PATH.parent.mkdir(exist_ok=True)
    file_exists = FEEDBACK_PATH.exists()

    row = {"timestamp": datetime.utcnow().isoformat()} | record

    with FEEDBACK_PATH.open("a", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDNAMES)
        if not file_exists:
            writer.writeheader()
        writer.writerow(row)
