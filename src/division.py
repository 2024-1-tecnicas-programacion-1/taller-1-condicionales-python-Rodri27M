def evaluar(dividendo, divisor):
    # TODO: Coloca aquí el código del ejercicio 3: Division
    cociente = 0
    residuo = 0

    if divisor == 0:
        respuesta = "Error. No se puede dividir en cero."
        return respuesta

    division = dividendo // divisor
    residuo = dividendo % divisor

    if residuo == 0:
        cociente += division
        respuesta = f"La división es exacta.\nCociente: {cociente}\nResiduo: {residuo}"
        return respuesta
    else:
        cociente += division
        respuesta = f"La división no es exacta.\nCociente: {cociente}\nResiduo: {residuo}"
        return respuesta

if __name__ == '__main__':
    print("Dividendo:", end="")
    dividendo = int(input())
    print("Divisor:", end="")
    divisor = int(input())

    respuesta = evaluar(dividendo, divisor)
    print(respuesta)
