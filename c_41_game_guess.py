## Riddle with bulces 

import random

print("Hi What is your name?")
print("Tell me: ")
username = input()

# Var to modification de game
time = 5
do = 0
done = 0
stop = 6

#mesege


print("Hi " + username + ",")
print("You have to riddle the number that i am thinking bewteen " +  str(stop) + " and 1")
print("Remenber that you have " + str(time) + " times")

# Generation a aleatori number
guess = random.randint(1, stop)


 
while do <= time:

    num = int(input("Try to guess: "))

    if num == guess: 
        print(username + " won ð The game have been finished!")
        done = 0
        print("""
        What do you want?
        A) Play again.
        B) Finish the game.
        """)
        option = input(">>> ")

        if option == "A":
            print("ð Try again, you have " + str(done) + "/" + str(time) + " Times ")
            do = 0
        if option == "B":
            print("ð You are a loser, you dont have more oportunities. Game over ðº.")
            break
###
    else: 
        if num > guess: 
            print("ðTry with number more small")
    if num < guess:
        print("ð Try with number bigger")
        do += 1
    if num != guess:
        print(username + " You loss")
        done += 1    
###                   
    if done > 5: 
        done = 0
        print("""
        What do you want?
        A) Play again.
        B) Finish the game.
        """)
        option = input(">>> ")

        if option == "A":
            print("ð Try again, you have " + str(done) + "/" + str(time) + " Times ")
            do = 0
        if option == "B":
            print("ð You are a loser, you dont have more oportunities. Game over ðº.")
            break

