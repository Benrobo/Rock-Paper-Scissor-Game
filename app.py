import random
import sys

op = ["rock", "paper", "scissors"]

print("""
""")

rand = random.randint(0, 2)

ai = op[rand]

aiscore = 0
userscore = 0

while True:
    user = input("enter your options ")
    if user == "":
        print("Program require  an input")
        break
    elif user == "rock" and ai == "paper":
        userscore -= 1
        aiscore += 1
        print("you loose")
        print("ai won")
    elif user == "paper" and ai == "rock":
        userscore += 1
        aiscore -= 1
        print("you win")
        print("ai loose")

    elif user == "paper" and ai == "scissors":
        userscore -= 1
        aiscore += 1
        print("you Loose")
        print("ai won")
    elif user == "scissors" and ai == "paper":
        userscore += 1
        aiscore -= 1
        print("you won")
        print("ai loose")

    elif user == "rock" and ai == "scissors":
        userscore += 1
        aiscore -= 1
        print("you win")
        print("ai loose")

    elif user == "scissors" and ai == "rock":
        userscore -= 1
        aiscore += 1
        print("you loose")
        print("ai won")

    elif user == "paper" and ai == "paper":
        userscore += 1
        aiscore += 1
        print("Draw")

    elif user == "rock" and ai == "rock":
        userscore += 1
        aiscore += 1
        print("Draw")
    elif user == "scissors" and ai == "scissors":
        userscore += 1
        aiscore += 1
        print("Draw")

    else:
        print("Sorry can only allowed valid game options. i.e 'rock ⛰️, paper 📃, scissors✂️' \n")
        sys.exit()

    print("User 👨‍" + str(userscore), '\n', "AI 🤖" + str(aiscore))
