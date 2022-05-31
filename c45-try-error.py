## Find error 

try:
    num = int(input("Give a number: "))
    nume = 2
    print(num / nume)

except ZeroDivisionError as err:
    print(err)
    print("You can not division between 0")   
except ValueError as err:
    print(err)
    print("Error, i dont know what is this")

else:
    print("There isnt error")

finally:
    print("This is the end")
