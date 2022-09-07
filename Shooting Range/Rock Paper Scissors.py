import random
import time

player = input("Rock, Paper, Scissors? ")
com = random.randint(1, 3)

if player == "Rock" or "rock":
    player = "Rock"
elif player == "Paper" or "paper":
    player = "Paper"
elif player == "Scissors" or "scissors":
    player = "Scissors"
else:
    print("Invalid input.")
    exit()

if com == 1:
    com = "Rock"
elif com == 2:
    com = "Paper"
else:
    com = "Scissors"

print("Rock...")
time.sleep(1)
print("Paper...")
time.sleep(1)
print("Scissors...")
time.sleep(1)
print("Shoot!")
time.sleep(2)
print("You chose " + player + ".")
time.sleep(1)
print("The computer chose...")
time.sleep(3)
print(com + "!")
time.sleep(1)

if player == com:
    print("It's a tie!")
elif player == "Rock" and com == "Paper":
    print("You lose!")
elif player == "Rock" and com == "Scissors":
    print("You win!")
elif player == "Paper" and com == "Rock":
    print("You win!")
elif player == "Paper" and com == "Scissors":
    print("You lose!")
elif player == "Scissors" and com == "Rock":
    print("You lose!")
elif player == "Scissors" and com == "Paper":
    print("You win!")
else:
    print("Error.")

