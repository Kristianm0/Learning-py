#Class _ Super

class Mammal: 
    def __init__(self, name):
        print('Its a animal with hot blood')
    
class Lion(Mammal):
    def __init__(self):
        print('Four legged animal')
        # super().__init__('Simba')
        Mammal.__init__(self, 'Simba')

new_lion = Lion()