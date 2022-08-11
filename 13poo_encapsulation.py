# Encapsulation

class Customer: 
    def __init__(self): 
        self.__code = 12345
    
    def getcode(self):
        return self.__code

    def __account(self):
        print('Prosecution account')

people = Customer()
print(people._Customer__code)
people._Customer__account()