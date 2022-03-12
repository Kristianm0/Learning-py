### UNIENDO VARIABLES Y CADENAS



krism = 102922
colina = "Colina"


# Esto es una manera de contatenar un valor numerico.
# 1) Tienes que convertir el numero en string.
# 2) Llamarlo  (obviamente).


krism = str(krism)

oso = "Kristian es una persona muy amable. " + krism + " es su nivel de amabilidad"

print (oso)

# Pero hay otra manera de hacerlo:
# Creamos el var con los datos que vamos llamar. En este caso "juego" y "krism".
# Creamos la var donde lo vamos a necesitar.
# Usamos al final la function "format" y entre los parentesis llamamos a las var con sus valores.
# Despues colocamos parentesis () donde querremos poner los valores. En este caso (krism, juego).
# Y luego solo llamas el var con la function. En este caso print.
# La difrencia entre los 2 metodos es que en este no se tiene que transformar las var a string porque ya lo hace el .format.
# Con .format lo pudes hacer, ejemplo:


juego ="Clash Royale"
juego1 = "Fornite"
juego2 = "Super Mario Bros"
juego3 = "Marvel Super Galaxy"
juego4 = 9282902923 

osos = "Kristian tiene {} monedas de {},".format(krism, juego4)
ososs = " Pero esto no es verdad"

print ((osos) + (ososs))

#Hay otra forma de hacerlo y es muy similar a la anterior, pero es mas intuitiva.

osos1 = "You are playing {a} right now".format(a=juego1)

print(osos1) 

#Otra forma mas

oso3 = f"Kristian tiene {juego4} monedas de {juego}"

print (oso3)

### Estas son las diferentes formas de cocatenar var ya sea con texto o con numero.