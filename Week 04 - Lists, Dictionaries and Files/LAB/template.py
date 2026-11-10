"""
RECORD CHECK  -  my version
===========================

Name  : Blessing Sesay
Lane  : AI
Date  : 23/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
def check_record(value, limit):
    """Calculate difference, percent, and status for a given value and limit."""
    diff = value - limit
    percent = (value / limit) * 100
    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"
    return diff, percent, status


def print_report(label, value, limit, diff, percent, status):
    """Print a bordered report for a single record."""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"Dataset      : {label}")
    print(f"Rows Loaded  : {value}")
    print(f"Rows Expected: {limit}")
    print(f"Difference   : {diff}")
    print(f"Percent      : {percent:.1f}%")
    print(f"Status       : {status}")
    print("=" * 34)


def load_records(path):
    """Read dataset,rows_loaded,rows_expected lines from a file and return a list of dicts."""
    records = []
    with open(path, "r", encoding="utf-8") as f:
        next(f)  # Skip the header row
        for line in f:
            line = line.strip()
            if not line:
                continue
            dataset, rows_loaded, rows_expected = line.split(",")
            records.append({
                "label": dataset.strip(),
                "value": float(rows_loaded.strip()),
                "limit": float(rows_expected.strip())
            })
    return records
# ====================================================================== STORE
try:
    records = load_records("records_sample.txt")
except FileNotFoundError:
    print("[Error] 'records_sample.txt' file not found. Starting with an empty list.")
    records = []
# =============================================================== PROCESS + OUTPUT
over_limit_count = 0
results_to_write = []

for r in records:
    diff, percent, status = check_record(r["value"], r["limit"])
    
    print_report(r["label"], r["value"], r["limit"], diff, percent, status)
    
    if status == "OVER LIMIT":
        over_limit_count += 1
    
    results_to_write.append(f"{r['label']},{status}\n")

if records:
    with open("survey_results_summary.csv", "w", encoding="utf-8") as f:
        f.write("label,status\n")
        f.writelines(results_to_write)
    print(f"\n[Saved] Results summary saved to 'survey_results_summary.csv'")

print(f"\nTotal datasets OVER LIMIT: {over_limit_count}")
# ==========================================================================
