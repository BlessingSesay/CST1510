# ADDITION QUIZ(
# STEP 1: Generate two single-digit integers for number 1 (e.g. 4), and numbwer 2 (e.g. 5)
# STEP 2: Prompt the student to answer, "What is 4 + 5?" (user input)
# STEP 3: Check whether the student's answer is correct. )

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

while True:
    sum = int(input(f"What is {number1} + {number2}? "))
    if sum == int(number1 + number2):
        print("CORRECT.")
        break
    else:
        print("INCORRECT, please try again.")

#%%
import random

number1 = random.randint(1,9)
number2 = random.randint(1,9)

while True:
    sum = int(input(f"What is {number1} + {number2}? "))
    if sum == int(number1 + number2):
        print("CORRECT.")
        break
    else:
        print("INCORRECT, please try again.")