import math

def cifrado_afin(texto, a, b):
    alfabeto = 'abcdefghijklmnñopqrstuvwxyz '
    texto_cifrado = ''
    for char in texto.lower():
        if char in alfabeto:
            y = (a * alfabeto.index(char) + b) % len(alfabeto)
            texto_cifrado += alfabeto[y]
    return texto_cifrado.upper()

def descifrado_afin(texto_cifrado, a, b):
    alfabeto = 'abcdefghijklmnñopqrstuvwxyz '
    texto = ''
    a_inv = pow(a, -1, len(alfabeto))
    for char in texto_cifrado.lower():
        if char in alfabeto:
            x = a_inv * (alfabeto.index(char) - b) % len(alfabeto)
            texto += alfabeto[x]
    return texto.upper()

while True:
    print("\n1. Cifrar texto")
    print("2. Descifrar texto")
    print("3. Salir")
    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        a = int(input("Ingresa el valor de a: "))
        while math.gcd(a, 28) != 1:
            print("El valor de a debe ser coprimo con 28. Por favor, intenta de nuevo.")
            a = int(input("Ingresa el valor de a: "))
        b = int(input("Ingresa el valor de b: "))
        texto = input("Ingresa la palabra a cifrar: ")
        texto_cifrado = cifrado_afin(texto, a, b)
        print('Texto cifrado:', texto_cifrado)

    elif opcion == 2:
        a = int(input("Ingresa el valor de a: "))
        while math.gcd(a, 28) != 1:
            print("El valor de a debe ser coprimo con 28. Por favor, intenta de nuevo.")
            a = int(input("Ingresa el valor de a: "))
        b = int(input("Ingresa el valor de b: "))
        texto_cifrado = input("Ingresa el texto cifrado a descifrar: ")
        texto_descifrado = descifrado_afin(texto_cifrado, a, b)
        print('Texto descifrado:', texto_descifrado)

    elif opcion == 3:
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Por favor, intenta de nuevo.")
