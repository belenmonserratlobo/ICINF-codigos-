lista = []

while True:
    print("Menu")
    print("1. Ingresar un elemento a la lista")
    print("2. Modificar elemento (según índice)")
    print("3. Eliminar elemento (según índice)")
    print("4. Eliminar último elemento de la lista")
    print("5. Buscar un elemento de la lista según el dato (devuelve el índice)")
    print("6. Mostrar todos los elementos de la lista")
    print("7. Salir")
    
    opcion = int(input("Ingrese opción: "))
    
    if opcion == 1:
        datito = input("Ingrese el elemento que quiere ingresar: ")
        lista.append(datito)
    elif opcion == 2:
        indice = int(input("Ingrese el índice del elemento que desea modificar: "))
        if 0 <= indice < len(lista):
            nuevoda = input("Ingrese el nuevo elemento: ")
            lista[indice] = nuevoda
        else:
            print("Índice fuera de rango.")
    elif opcion == 3:
        indice = int(input("Ingrese el índice del elemento que desea eliminar: "))
        if 0 <= indice < len(lista):
            lista.pop(indice)
        else:
            print("Índice fuera de rango.")
    elif opcion == 4:
        if lista:
            lista.pop()
        else:
            print("La lista está vacía.")
    elif opcion == 5:
        busca = input("Ingrese el elemento que busca: ")
        if busca in lista:
            indice = lista.index(busca)
            print("El dato se encuentra en la posición", indice)
        else:
            print("Elemento no encontrado.")
    elif opcion == 6:
        print(lista)
    elif opcion == 7:
        print("Se terminó el programa.")
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")
