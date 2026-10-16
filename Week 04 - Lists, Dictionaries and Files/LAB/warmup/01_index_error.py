# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

labels = ["R-001", "R-002", "R-003"]
try:
    result = (labels[2])
except IndexError:
    print("Index out of range. Please check the index and try again.")
else:
    print(f"Index is valid, {result}")
