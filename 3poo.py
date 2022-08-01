from wsgiref.validate import InputWrapper


class Math: 
    def plus(self):
        self.n1 = 2 
        self.n2 = 3

s = Math()
s.plus()


class Clothes:
    def __init__(self):
        self.brand = "Willow"
        self.size = "S"
        self.color = "Red"

Shirt = Clothes()

class Calculation:
    def __init__(self,n1,n2):
        self.plus = n1 + n2 
        self.subtraction = n1 - n2 
        self.division = n1 / n2 
        self.multiplication = n1 * n2

operation = Calculation(2,3)
print(operation.multiplication)
