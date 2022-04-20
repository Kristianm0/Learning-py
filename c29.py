### Funciones

#We ask the years by another input,  and use round to have the whole number without  decimal, and we use float to have the number and not have a string.

# El input es para pedirles datos al usuarios, y que se tiene que almacenar en un var.

def waves():
    print("Your name")
    name = input()
    print ("How old are you")
    year = round(float(input()))
    print(f"Hi user: {name}, that have {year} year old")
    print("""
    Some else that you want tell me?
    1) Yes i have to tell you something else 🖐️.
    2) No i do not have to tell you something else 😊.
    3) Reiniciar.
    4) Surprise.
    """)

# The 1 have to be string not number.
    print("Choose a number:")
    ee = input()
    if ee == "1":
        print("Tell me:")
        input()
        print("Thanks for your honesty.")   
    elif ee == "2":
        print("Ok, Thanks for your honesty.")
    elif ee == "3":
        waves()
    elif ee == "4":
        print(name* 9999990)  
    else: 
        print("What is this? I dont know to do.")

print("Hi my name is Krism and i have 12 years old and you?")
waves()

