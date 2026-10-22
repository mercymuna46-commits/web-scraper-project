"""Storage stage: persist scraped records."""
import csv
import json
import os


def save_to_csv(records: list[dict], path: str) -> None:
    """Write records to a CSV file."""
    if not records:
        print(f"[STORAGE] No records to write to {path}")
        return
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(records[0].keys()))
        writer.writeheader()
        writer.writerows(records)
    print(f"[STORAGE] Wrote {len(records)} records to {path}")


def save_to_json(records: list[dict], path: str) -> None:
    """Write records to a JSON file."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(records, f, indent=2, ensure_ascii=False)
    print(f"[STORAGE] Wrote {len(records)} records to {path}")
