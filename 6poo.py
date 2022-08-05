#inheritance

class Pokemon:
    def __init__(self, name, tipo):
        self.name = name
        self.tipo = tipo
    
    def description(self):
        return '{} is a pokemon of type {}'.format(self.name, self.tipo)

class Pikachu (Pokemon):
    def attack(self, tipoattack):
        return '{} Attack type: {} '.format(self.name, tipoattack)

class Amoka(Pokemon):
    def ataque(self, tipoattack):
        return '{} Attack type: {}'.format(self.name, tipoattack)

new_pokemon = Pikachu('Amus', 'eletreic')
print(new_pokemon.description())
print(new_pokemon.attack('Impact thunder'))





