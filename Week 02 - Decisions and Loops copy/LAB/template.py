"""
RECORD CHECK  -  my version
===========================

Name  : Blessing Sesay
Lane  :  AI
Date  : 02/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""


# ==================================================================== INPUT
over_limit_count = 0

while True:
    label = input("Enter dataset name (or type 'quit' to stop): ")
    if label == "quit":
        break
    value = float(input("Enter rows loaded: "))
    limit = float(input("Enter rows expected: "))

# ================================================================== PROCESS
difference = limit - value
percent = (value / limit) * 100

if percent >= 100:
        status = "OVER LIMIT"
        over_limit_count += 1
elif percent >= 90:
        status = "WARNING"
else:
        status = "OK"
# =================================================================== OUTPUT
print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print(f"Rows Loaded  : {value:>8.2f}")
print(f"Rows Expected: {limit:>8.2f}")
print(f"Difference   : {difference:>8.2f}")
print(f"Percent      : {percent:>8.2f} %")
print(f"Status       : {status:>8}")

print("=" * 34)
# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every variable name says what it holds
