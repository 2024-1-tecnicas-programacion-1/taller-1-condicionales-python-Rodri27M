def evaluar(num_victorias_a, num_victorias_b):
    # TODO: Coloca aquí el código del ejercicio 1: Set de tenis
    resta = abs(num_victorias_a - num_victorias_b)

    if resta > 2 or resta == 0:
        print("Inválido")
        return ""

    if (num_victorias_a >= 6 or num_victorias_b >= 6) and resta <= 2:
        if resta == 1 and (num_victorias_a < 6 or num_victorias_b < 6):
            print("Aún no termina")
            return ""
        
        if 0 < resta <= 2:
            if num_victorias_a > num_victorias_b:
                print("Ganó A")
                return ""
            elif num_victorias_b > num_victorias_a:
                print("Ganó B")
                return ""
    else:
        print("Aún no termina")
        return ""

    return ""
if __name__ == '__main__':
    print("Los juegos ganaddor por A:", end="")
    num_victorias_a = int(input())
    print("Los juegos ganaddor por B:", end="")
    num_victorias_b = int(input())

    respuesta = evaluar(num_victorias_a, num_victorias_b)
    print(respuesta)
