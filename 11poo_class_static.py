#method static 

import math

class Cake: 
    def __init__(self, ingredients, size):
        self.ingredients = ingredients
        self.size = size
    
    def __repr__(self):
        return(f'Cake({self.ingredients}, 'f'{self.size})')
    
    def area(self):
        return self.size_area(self.size)

    def __repr__(self):
        return f'Cake({self.ingredients !r})'
    
    @staticmethod
    def size_area(A):
        return A ** 2 * math.pi

cake_new = Cake(['Eggs', 'Salt', 'Butter'],4)
print(cake_new.size_area(2))

    
    #@classmethod
    #def Chocolate_Cake(cls):
     #   return cls(['Milk', 'Cacao', 'Sugar'])
    
    #@classmethod
    #def Vanilla_cake(cls):
     #   return cls(['Milk', 'Vanilla', 'Sugar'])

#print(Cake.Chocolate_Cake())

