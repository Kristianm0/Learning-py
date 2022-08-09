# F - string()
# formart %

#course = "Python"
#print("how to % s "%course)

#name = "Amoka"
#years = 2
#print("Hi i am, % s and i am % s years old"%(name, years))

#print('How are you? My name is {}, and i am {} years old.'.format(name, years))
#print(f'Hi i am krism {name} and i am {years} years old. ')

class Student:
    def __init__(self, name, last_name, year):
        self.name = name
        self.last_name = last_name
        self.year = year
    
    def __str__(self):
        return f'{self.name} {self.last_name} {self.year}'

new_student = Student('Amokar', 'Colins', 39)
print(f'{new_student}')

