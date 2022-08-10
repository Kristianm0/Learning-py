#Polymorphism

#class Auto:
 #   wheel = 4
  #  def displacement(self):
   #     print('The car is displacement in four wheels')

#class motorcycle:
 #   wheel = 2
  #  def displacement(self):
   #     print("The motorcycle is displacement in two wheels")

class Animals: 
    def __init__(self, name):
        self.name = name
    def type_animal(self):
        pass
class lion(Animals):
    def type_animal(self):
        print('Wild Animal')

class Dog(Animals):
    def type_animal(self):
        print("domestic animals")

new_animal = lion('Simba')
new_animal.type_animal()

new_animal = Dog('Max')
new_animal.type_animal()