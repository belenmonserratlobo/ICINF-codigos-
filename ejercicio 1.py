lista=[]
for x in range(3):
    num=int(input("Ingrese un numero a la lista: "))
    lista.append(num) 
for i in range(len(lista)-1, -1, -1):
    print(lista[i])
