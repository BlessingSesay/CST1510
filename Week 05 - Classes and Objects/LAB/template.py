"""
RECORD CHECK  -  my version
===========================

Name  : Blessing Sesay
Lane  : AI
Date  : 06/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ====================================================================== CLASS
class Record:
    """Represents a survey record and its loading status."""

    def __init__(self, dataset, rows_loaded, rows_expected):
        """create a record with dataset name, rows loaded, and rows expected."""
        self.dataset = dataset
        self.rows_loaded = float(rows_loaded)
        self.rows_expected = float(rows_expected)

    def status(self):
        """Calculate percentage and return status update."""
        percent = (self.rows_loaded / self.rows_expected) * 100
        if percent >= 100:
            return "OVER LIMIT"
        elif percent >= 90:
            return "WARNING"
        else:
            return "OK"
# ==================================================================== RECORDS
def load_records(path):
    loaded_records = []
    with open(path, "r", encoding="utf-8") as f:
        # Skip the header row
        next(f)
        for line in f:
            line = line.strip()
            if not line:
                continue
            dataset, rows_loaded, rows_expected = line.split(",")
            record = Record(dataset.strip(), rows_loaded.strip(), rows_expected.strip())
            loaded_records.append(record)
    return loaded_records

records = load_records(r"C:\Users\bless\Documents\CST1510\Week 05 - Classes and Objects\LAB\survey_records.csv")
# ==================================================================== OUTPUT
over_limit_total = 0

for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.dataset}")
    print("=" * 34)
    
    current_status = record.status()
    
    if current_status == "OVER LIMIT":
        over_limit_total += 1

    print(f"Dataset      : {record.dataset}")
    print(f"Rows Loaded  : {record.rows_loaded}")
    print(f"Rows Expected: {record.rows_expected}")
    print(f"Status       : {current_status}")
    print("=" * 34)
# ==========================================================================
print(f"\nTotal datasets OVER LIMIT: {over_limit_total}")