#Clases y objetos

class Jugadores:
    #definimos los atributos
    def __init__(self, nombre, edad, equipo):
        self.nombre = nombre
        self.edad = edad 
        self.equipo = equipo

#Agregamos valores a las clase
jugador_1 = Jugadores("Andres Inista", "48" , "Barcelona FC")
#Llamos los valores a la clase
print(jugador_1.nombre, jugador_1.edad, jugador_1.equipo) 


