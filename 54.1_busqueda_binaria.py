#Busqueda binaria 
# - Hacer que el usuario pueda buscar los valores.✅
# -- Hacer que el usuario ingrese valores ✅
# -- Que los valores que ingreso el usuario se sumen a la lista.✅

# - bucle__ Agregar un ciclo infinito para realizar todas las busquedas y que se termine el ciclo.✅
# -- seguir pidiendo a usuario que busque un numero. ✅
# -- mostrar un mensaje de seguir o detener el codigo. ✅
#

#Creamos una lista

print("Hola, vamos a buscar el numero que quieras 🙂")
lo = (input("Di ok si estas de acuerdo >>> "))
lo = lo.upper()


lista = [1, 0 , 89, 90, 100, 2, 16, 3, 34, 4543, 322, 39, 6, 65, 565, 569, 0, 895, 940]
lista.sort()


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
        return f"El valor {valor} no fue encontrado 🤔"
    else:
        return f"El valor {valor} se encuentra en la posicion {res_busqueda} 😉"

while lo == "OK":
    print("""
    1. Buscar valor.
    2. Agregar valor. 
    3. Ver la lista.
    4. Detener el programa.
    """)
    
    user = int(input(" Tu eliges >>> "))
    
    if user == 1:
        print("¿Que valor quieres buscar?")
        var = int(input(">>> "))
        print(buscar_valor(var))
    
    elif user == 2:
        print("¿Que numero quieres agregar?")
        add = int(input(">>> "))
        add = lista.append(add)
    
    elif user == 3:
        print("Esta es la lista")
        print(lista)
    
    elif user == 4:
        print("El programa esta apagado.")
        break