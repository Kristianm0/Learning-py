#serializar

import pickle

# estudiante = [
# "Marcos",
# "Carla",
# "Agustin",
# "Pedro",
# "Maria"
# ]

# archivo = open("estudiantes", "wb")

# pickle.dump(estudiante, archivo)

# archivo.close()
# del archivo

archivo = open("estudiantes", "rb")
lista_estudiante = pickle.load(archivo)
print(lista_estudiante)