#  Class to add value ------------------
class Phone:
    def __init__(self, name, color, model):
        print("Tell me the caraters of your phone please")
        self.name = input("Name >>> ")
        self.color = input("Color >>> ")
        self.model = input ("Model >>> ")

#new_phone = Phone("", "" ,"")
#print((new_phone.name), (new_phone.color), (new_phone.model))

#Class to delete value ------------------
# 2 Otro metodo que permita eliminar cursos

class Laptop:
    def __init__(self, color, memory, processor): 
        self.color = color
        self.memory = "16 RAM"
        self.processor = "Ryzen 5"

new_laptop = Laptop("red","","")
#print(new_laptop.color)
del[new_laptop.color]
#print(new_laptop.color)

#Class to send value and delete

class Singer: 
    def __init__(self, name): 
        self.name = name 

print("Tell me your favorite singer from Mexico")

new_singer = Singer(name = input("What is your name? >>> "))
print(new_singer.name +"is the singer")

print("Do you want to change the name?")

ask = print(""" 
1. Yes
2. No 
""")
ask = input(str(">>> "))

if ask == "1":
    del[new_singer.name]
    print("Tell me the new singer")
    
    new_singer = Singer(name = input("What is the new name >>> "))
    print("The new name: ")
    print(new_singer.name + " is the new singer")

if ask == "2":
    print("Ok")
    print(new_singer.name + " is the singer")

