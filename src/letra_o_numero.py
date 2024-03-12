def evaluar(caracter):
    # TODO: Coloca aquí el código del ejercicio 4: Letra o número
    if caracter.isalpha():
     if caracter.isupper():
        print("Es una letra mayúscula.")
     elif caracter.islower():
        print("Es una letra minúscula.")
    else:
     if caracter.isdigit():
        print("Es un número.")
     else:
        print("No es ni una letra ni un número.")
    return "";

if __name__ == '__main__':
    print("Caracter:", end='')
    caracter = input()
        
    respuesta = evaluar(caracter)
    print(respuesta)
