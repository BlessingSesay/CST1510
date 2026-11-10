# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

def check_record(value, limit):
    """Calculate status for a given value and limit."""
    percent = (value / limit) * 100
    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"
    return status

result = check_record(87, 100)