#class and objetcs


class Student:
    def __init__(self, name, last_name , years):
        self.name = name
        self.last_name = last_name
        self.years = years
        self.status = True

    

Estudiante = Student("Amoka", "Collins", 3)

#print(Estudiante.name)

class Desk: 
    def __init__(self, table, foot, color):
        self.table = table 
        self.foot = foot
        self.color = color 

new_desk = Desk("Large table", "4 foot", "Blue with black")
#print(new_desk.table)

class Planeta:
    def __init__(self, color, name, years, ):
        self.color = color
        self.name = name
        self.years = years

new_planet = Planeta("Blue", "Jamoka", 738.911)
print(new_planet.name)

new_planet2 = Planeta("Red", "Jorodo", 932.239)
print(new_planet2.name)

new_planet3 = Planeta("Orange", "Jakatalina", 223.121)
print(new_planet3.name)