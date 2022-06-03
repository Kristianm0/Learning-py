## Guess but from the compu

import random


def guess_compu(x):
    print("__________________")
    print("Welcome to the game")
    print("What is your name 👇")
    nameu = input()
    print("Hi " + nameu + " I am compu, and I will be the player B to game.")
    print("Let `s go to game")
    print("Choose a number between 1 and "+ x + "to the computer (me) try to guess the number")

    stop_up = 1
    stop_down = x

    answer = ""
    while answer !="c":
        if stop_down != stop_up:
            predition = random.randint(stop_down, stop_up)
        else:
            predition = stop_down 

            answer = input("My predition is "+(predition)+ "if it is too high choose (A), but it is too down choose (B), and if it is correct choose (C)").lower()

            if answer == "a":
                stop_up = predition - 1
            elif answer == "b":
                stop_down = predition + 1
            else:
                print("I won 🚀")                