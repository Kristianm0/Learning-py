#inheritance 1.0


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def hum_description(self):
        return '{} is a {}'.format(self.name, self.age)

class Human1 (Human):
    def age(self, age):
        return '{}  is the best human in the world, your ages is {}'.format(self.name, age)

new_human = Human1('Amokagg', '13')
print(new_human.hum_description())
print(new_human.age("years old"))