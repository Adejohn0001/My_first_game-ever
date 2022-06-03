import random
from secrets import choice
from ssl import Options

user_wins = 0
computer_wins = 0

option =["rock", "paper", "scissors"]

mylist = [0, 1, 2]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to Quit: ").lower()
    if user_input == "q":
        break
    if user_input not in option:
        continue

    random_word = random.choice(mylist)
    #rock: 0, paper: 1, scissor: 2
    computer_pick = option[random_word]
    print("Computer picked", computer_pick +".")

    if user_input =="rock" and computer_pick =="scissors":
        print("You won!")
        user_wins += 1

    if user_input =="rock" and computer_pick =="rock":
        print("A tie, Rock beats Scissors, Paper beats Rock and Scissors beats Paper!!!.")
        user_wins += 1


    elif user_input =="paper" and computer_pick =="rock":
        print("You won!")
        user_wins += 1

    elif user_input =="scissors" and computer_pick =="paper":
        print("You won!")
        user_wins += 1

    elif user_input =="paper" and computer_pick =="paper":
        print("a tie, Rock beats Scissors, Paper beats Rock and Scissors beats Paper!!!.")
        user_wins += 1

    elif user_input =="scissors" and computer_pick =="scissors":
        print("a tie, Rock beats Scissors, Paper beats Rock and Scissors beats Paper!!!.")
        user_wins += 1

    else:
        print("You lost")
        computer_wins += 1

print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Goodbye!!")