"""
RECORD CHECK  -  my version
===========================

Name  : Blessing Sesay
Lane  : AI
Date  : 10/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
def parse_line(raw_line: str) -> dict:
    """Clean and parse a raw messy line into a dictionary."""
    cleaned_line = raw_line.strip()
    if not cleaned_line:
        return {}
    
    parts = cleaned_line.split(",")
    record = {}
    
    for i, part in enumerate(parts):
        part = part.strip()
        if "=" in part:
            key, val = part.split("=", 1)
            key = key.strip().lower()
            val = val.strip().lower()
            try:
                val = int(val)
            except ValueError:
                try:
                    val = float(val)
                except ValueError:
                    pass
            record[key] = val
        else:
            if i == 0:
                record["survey"] = part.lower()
            else:
                record[f"field_{i}"] = part.lower()
                
    return record

def status_of(record: dict) -> str:
    """Evaluate record fields and return FLAGGED or OK status."""
    rating = record.get("rating", 5)
    age = record.get("age", 25)
    
    if rating < 3 or age < 18:
        return "FLAGGED"
    return "OK"
# ====================================================================== INPUT
filename = "records.txt"
raw_records = []

try:
    with open(filename, "r") as file:
        raw_records = file.readlines()
except FileNotFoundError:
    print(f"Error: '{filename}' was not found. Please create it in the LAB folder.")
# =============================================================== PROCESS + OUTPUT
total_records = 0
flagged_count = 0

for raw_record in raw_records:
    if not raw_record.strip():
        continue
    
    total_records += 1
    cleaned_dict = parse_line(raw_record)
    status = status_of(cleaned_dict)
    
    if status == "FLAGGED":
        flagged_count += 1
        
    print(f"Cleaned: {cleaned_dict} | Status: {status}")
# ==========================================================================
print(f"\nSummary: Processed {total_records} records, {flagged_count} flagged.")