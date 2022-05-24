### Infinity loops 

#star infinity loop

while True:
    print("Enter a number to continue")
    print("""
    1) Star the loop.
    2) Stop the loop.
    """)
    option = input(">>> ")

    if option == "1":
        print("👌")
    if option == "2":
        print("😒")
        break
    