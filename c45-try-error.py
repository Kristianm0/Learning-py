## Find error 


while True:
    try:
        print("Let's go to division your number 💣")

        print("Give me the first value")
        num1 = int(input("👉 "))

        print("Give me the secound value")
        num2 = int(input("👉 "))

        print("Your result is 👇: ")
        print(num1 / num2)

    except ZeroDivisionError as err:
        print(err)
        print("You can not division between 0")   
    except ValueError as err:
        print(err)
        print("Error, i dont know what is this")

    else:
        print("Your division has been done succefully 🤝")
        
    print("""Do you wants to play again
    1) Yes.
    2) No.
    """)
    op = input("👉 ")
    
    if op == 2:
        break




