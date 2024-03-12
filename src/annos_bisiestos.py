def evaluar(anno):
    # TODO: Coloca aquí el código del ejercicio 2: Años bisiestos
    residuo = False

    if (anno % 4 == 0 and anno % 100 != 0) or (anno % 400 == 0):
        residuo = True

    if residuo:
        print(f"{anno} es bisiesto")
    else:
        print(f"{anno} no es bisiesto")

if __name__ == '__main__':
    print("Año:", end="")
    anno = int(input())

    evaluar(anno)
