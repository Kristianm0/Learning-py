# Example  of inheritance

# Definimos la neustra clase, su contructor y sus atributos.
class Calculation: 
    def __init__(self, number): 
        self.n = number
        self.d = data = [0 for i in range(number)]
    
    def enter_data(self):
        self.data = [int(input("Enter data "+ str(i + 1)+ "= ")) for i in range(self.n)]

class op_basics(Calculation):
    def __init__(self):
        Calculation.__init__(self, 2)
        
    def plus(self):
        a,b = self.data
        p = a + b 
        print("The result is; ", p)
    
    def subtraction(self):
        a,b = self.data
        s = a - b 
        print("The result is; ", s)

class Root(Calculation):
    def __init__(self):
        Calculation. __init__(self, 1)
    
    def square(self):
        import math
        a, = self.data
        print("The result is; ", math.sqrt(a))

example = Root()
print(example.enter_data())
print(example.square())
