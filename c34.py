## Calculadora 2.0

num1 = float(input("Give a number: "))
op = input("Give a operation: ")
num2 = float(input("Givr another number: "))

if op == "+":
    sum = num1 + num2
    print("The plus is: " + str(sum))
elif op == "-":
    sub = num1 - num2
    print("The subtractions is: " + str(sub))  
elif op == "*":
    mul = num1 * num2
    print("the multiplication is:" + str(mul))
elif op == "/":
    div = num1 / num2
    print("The division is: " + str(div))
else:
    print("I dont Know what is that")