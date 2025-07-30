import random

user = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: ")

if user == "0":
    print("You choose rock")
elif user =="1":
    print("You choose paper")
elif user=="2":
    print("You choose Scissors")
else:
    print("Invalid input")

item= ["Rock","Paper","Scissors"]
cmp = random.choice(item)
print(f"Computer choose {cmp}")

if cmp=="Rock" and user=="0":
    print("Draw!")
elif cmp=="Rock" and user=="1":
    print("You win")
elif cmp == "Rock" and user == "2":
    print("You lose!")

elif cmp == "Paper" and user == "0":
    print("You lose!")
elif cmp == "Paper" and user == "1":
    print("Draw!")
elif cmp == "Paper" and user == "2":
    print("You win!")

elif cmp == "Scissors" and user == "0":
    print("You win!")
elif cmp == "Scissors" and user == "1":
    print("You lose!")
elif cmp == "Scissors" and user == "2":
    print("Draw!")