from turtle import color


class Animals:
    animal = "Dog"
    age = 4
    name = "Luis"
    sexo = "Male"
    color = "brown"

dog = Animals()
delattr(Animals, "color")
print(Animals.name)
