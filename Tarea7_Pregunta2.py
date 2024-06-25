palabras = []

while True:
    palabra = input("Ingresa una palabra: ")
    if palabra == "":
        break
    palabras.append(palabra)

print("Cantidad de caracteres 'A' o 'a' en cada palabra:")
for palabra in palabras:
    contador_a = 0
    for letra in palabra:
        if letra.lower() == 'a':
            contador_a += 1
    print(palabras,":", contador_a)





