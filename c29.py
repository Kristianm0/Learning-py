### Funciones

#We ask the years by another input,  and use round to have the whole number without  decimal, and we use float to have the number and not have a string.

# El input es para pedirles datos al usuarios, y que se tiene que almacenar en un var.

def waves():
    print("Your name")
    name = input()
    print ("How old are you")
    year = round(float(input()))
    print(f"Hi user: {name}, that have {year} year old")
waves()
