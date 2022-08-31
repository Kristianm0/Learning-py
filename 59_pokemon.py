#juego pokemon 

import random

class Pokemon:
    def __init__(self, name, attack):
        self.name = name 
        self.attack = attack
        self.life = 100 
    
    def win(self):
        print(f"{self.name} Won this battle")
        print("Good look the next time")

Amokrus = Pokemon("Amokrus", 1)
Rodosh = Pokemon("Rodosh", 1)

Amokrus.life = 1500
Rodosh.life = 1500


print("The battle has been initiated")

print("About the pokemos:" )
#Amokrus
print("1. 🐕 Amokrus: ")
print(f"💥 The attack is bitus with {Amokrus.attack} of the power") 
print(f"❤️  The life is {Amokrus.life}")
print("")

#Rodosh
print("2. 😺 Rodosh: ")
print(f"💥 The attack is clawer with {Rodosh.attack} of the power")
print(f"❤️  The life is {Rodosh.life}")
print("")

print("The firts number is the pokemon to play firts")

turn = random.randint(1, 2) 
print(turn)

while Amokrus.life > 0 and Rodosh.life > 0:
    if turn == 1:
        print(f"😺 Rodosh attack tp {Amokrus.name} with clawer {Rodosh.attack} 💥")
        Amokrus.life = Amokrus.life - Rodosh.attack
        turn = 2
        print(f"🐕 The life of Amokrus is {Amokrus.life} ❤️")
        print("")

    else: 
        print(f"🐕 Amokrus attack to {Rodosh.name} with bitus {Amokrus.attack}💥" )
        Rodosh.life = Rodosh.life - Amokrus.attack 
        turn = 1
        print(f"😺 The life of Rodosh is {Rodosh.life} ❤️")
        print("")

#Vemos quien perdio o gano.
if Amokrus.life <= 0:
    Rodosh.win()

else:
    Amokrus.win()

