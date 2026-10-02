"""
RECORD CHECK  -  my version
===========================

Name  : Blessing Sesay
Lane  : AI
Date  : 27/09/026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
# ==================================================================== INPUT
dataset_name = input("Enter the dataset name: ")
rows_loaded = float(input("Enter the number of rows loaded: "))
rows_expected = float(input("Enter the number of rows expected: "))
# ================================================================== PROCESS
difference = rows_expected - rows_loaded
percent = (rows_loaded / rows_expected) * 100
# =================================================================== OUTPUT
print()
print("=" * 34)
print(f" RECORD CHECK  -  {dataset_name}")
print("=" * 34)
print(f"Rows Loaded : {rows_loaded:>10.2f}")
print(f"Rows Expected : {rows_expected:>10.2f}")
print(f"Difference : {difference:>+10.2f}")
print(f"Percentage of Rows Loaded : {percent:>10.2f}%")
print(f"Percentage of Rows Remaining : {100 - percent:>10.2f}%") #Calculated the percentage of rows remaining to be loaded as they may want to understand the success/failure rate of the load.
print("=" * 34)
# ==========================================================================
