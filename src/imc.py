def evaluar(peso, estatura, edad):
    # TODO: Coloca aquí el código del ejercicio 8: Índice de masa corporal
     IMC = int(peso / estatura ** 2)
    
     if edad < 45:
        if IMC < 22.0:
            print("bajo")
        elif IMC >= 22.0:
            print("medio")
     elif edad >= 45:
        if IMC < 22.0:
            print("medio")
        elif IMC >= 22.0:
            print("alto")
     return "";

if __name__ == '__main__':
    print("Peso:", end="")
    peso = int(input())
    print("Estatura:", end="")
    estatura = float(input())
    print("Edad:", end="")
    edad = int(input())
        
    respuesta = evaluar(peso, estatura, edad)
    print(respuesta)
