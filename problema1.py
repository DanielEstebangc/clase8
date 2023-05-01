def sumar_5_enteros():
    #definicion de variables
    lista = []
    contadorwhile = 0
    tamano = 5
    suma = 0

    # Ingresamos los numeros
    while contadorwhile < tamano:
        lista.append(int(input("ingrese el numero" + str(contadorwhile+1) + ": ")))
        contadorwhile += 1

    # Sumamos los numeros
    contadorwhile = 0
    while contadorwhile < tamano:
        suma += lista[contadorwhile]
        contadorwhile += 1

    print("los numeros de la lista son")
    for numero in lista:
        print(numero,end=', ')

    print("\nla suma de todos los elementos es:")
    print(suma)