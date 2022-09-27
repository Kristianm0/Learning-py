## Expresiones regulares para buscar texto

import re

def run():
    cadena = "Hola estudiantes de academia coder. En academiaCoder los estudiantes aprenderan programacion."
    buscar = "estudiantes"

    buscado = re.search(buscar, cadena)

    bu = re.findall(buscar, cadena)
    print(bu)
    print(len(bu))

    split = re.split(" ", cadena)
    print(split)

    sub = re.sub(buscar, "usuario", cadena)
    print(sub)

        # print(buscado)
        # print(buscado.start())
        # print(buscado.end()-1)
        # print(buscado.span())
        # print(buscado.group())

if __name__ == "__main__":
    run()