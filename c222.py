### Calculadora simple.

# Definimos las variables donde van a ir los valores.
# Esto se hace con:
# 1) Float convierte el dato en numero. 
# 2) Input pide y recibe informacion del usuario.

def calculation():
    print("The calculation is ready to have values, please:")
    n1 = float(input("Give the A) number: "))
    n2 = float(input("Give the B) number: "))
    
    option = 0
    print("""
        1) Add the two values.
        2) Subtraction the two values.
        3) Multiply the two values.
        4) Divide the two values.
        5) Resest the calculation.
        """)
    option = int(input("Choose a option: "))
    
    if option == 1:
        print("This is the result of the add")
        print(n1 + n2)
    elif option == 2:
        print("This is the result of the subtraction")
        print(n1 - n2)
    elif option == 3:
        print("This is the result of the Multiply")
        print(n1 * n2)
    elif option == 4:
        print("This is your result of the divide")
        print(n1 / n2)
    elif option == 5:
        calculation()
    else: 
        print("I dont kwon what is this")

print("Simple Calculation")
print("Write OK exactly to star: ")
m = input()
if m == "OK": 
    calculation()
else: 
    print("Write OK or leave here.")
