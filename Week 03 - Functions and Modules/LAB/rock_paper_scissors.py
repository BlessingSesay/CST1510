## Rock, Paper, Scissors
"""""
**Uses:** functions, `return`, `random.randint()`

1. At the top of your file, write `import random`.
2. Define a function called `get_computer_choice()`.
3. Inside it, create a variable `number` and set it to `random.randint(0, 2)`.
4. Use `if`/`elif`/`else` to check `number`:
   - if it is `0`, return `"rock"`
   - if it is `1`, return `"paper"`
   - otherwise, return `"scissors"`
5. Define a function called `decide_winner(user_choice, computer_choice)`.
6. Inside it, if `user_choice` equals `computer_choice`, return `"draw"`.
7. Add an `elif` that returns `"user"` if the user wins
   (rock beats scissors, paper beats rock, scissors beats paper).
8. Add an `else` that returns `"computer"`.
9. Outside the functions, use `input()` to ask the user for their choice
   and store it in a variable called `user_choice`.
10. Call `get_computer_choice()` and store the result in `computer_choice`.
11. Print the computer's choice.
12. Call `decide_winner(user_choice, computer_choice)` and store the result
    in `winner`.
13. Print who won.
"""""

import random

def get_computer_choice():
    number = random.randint(0,2)
    
    if number == 0:
        return "rock"
    elif number == 1:
        return "paper"
    else:
        return "scissors"

def decide_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "draw"
    elif user_choice == "rock" and  computer_choice == "scissors":
        return "user"
    elif user_choice == "paper" and  computer_choice == "rock":
        return "user"
    elif user_choice == "scissors" and  computer_choice == "paper":
        return "user"
    else:
        return "computer"


computer = get_computer_choice()
print(computer)

user = input("Enter your choice: ")

winner = decide_winner(user, computer)
print(winner)