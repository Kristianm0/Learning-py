## constructor method 

class People:
    pass 
    def __init__(self, name, year):
        self.name = name 
        self.year = year
    def description(self):
        return '{} have {} years old'.format(self.name,self.year)
    
    def comment(self, sentences):
        return '{} say: {}'.format(self.name, sentences)

doctor = People('Jose', 28)
print(doctor.description())
print(doctor.comment('Hi, how are you?'))