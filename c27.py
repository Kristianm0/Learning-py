### FUNCIONES DE LISTAS

num = [5, 10, 55, 300, 3, 1, 90]
fruits = ["Orange", "Apple", "Banana", "Pear", "Lemon", "Pieneapple"]

#print(len(fruits))

# Para agregar un dato más al final list:
#fruits.append("Lemon")

# Para remplazar un dato de la lista:
fruits[1] = "Apple 2"

# Para sumar listas
# Metodo 1: list2 = num + fruits

#num.extend(fruits)

# Para añadir un dato en una lista:
fruits.insert(1,"Grapes")

# Para remover un dato en la lista
fruits.remove("Banana")

# Para limpar o borrar los datos de una lista:
#fruits.clear()

# Para encontrar una posicion de datos:
#print(fruits.index("Grapes"))

# Para contar un dato:
#print(fruits.count("Banana"))

#Para darle reversa a una lista
fruits.reverse()

#Para ordenar una lista de modo alfabetico, pero esta funcion tambien sirve para ordernar de mayor a menor
fruits.sort()
num.sort()

# Para hacer una copia y almacenarlas en otra var:
fruits772 = fruits.copy()

print(fruits772)