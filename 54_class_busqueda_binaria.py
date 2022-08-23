#Busqueda binaria 

#Creamos una lista
lista = [1, 0 , 89, 90, 100, 2, 16, 3, 34, 4543, 322, 39, 6, 65, 565, 569, 00, 895, 940]

#Ordenamos la lista
lista.sort()
print (lista)

#Buscar el punto medio.
# Comprobar si el punto medio es el numero que buscamos.
# Si el numero es menor al que buscamos aumentamos 1 sobre el punto medio.
# Si el numero es mayor al que buscamos restamos 1 sobre el punto medio.
# Si inicio es igual, entonces el numero no esta en la lista.


def busqueda_binaria(valor):
    inicio = 0 
    fin = len(lista) - 1
    while inicio <= fin: 
        puntero = (inicio + fin) // 2 
        if valor == lista[puntero]:
            return puntero
        elif valor > lista[puntero]:
            inicio = puntero + 1
        else:
            fin = puntero - 1
    return None

def buscar_valor(valor):
    res_busqueda = busqueda_binaria(valor)
    if res_busqueda == None:
        return f"El valor {valor} no fue encontrado"
    else:
        return f"El valor {valor} se encuentra en la posicion {res_busqueda}"

print(buscar_valor(1600))