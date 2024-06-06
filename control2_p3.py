lista=[]

while True:
    palabra=input("Ingrese palabra: ")
    lista.append(palabra)
    if palabra=="":
        break
pos=0
for i in range(len(lista)):
    if i == 0:
        menor= len(lista[i])
    else:
        if len(lista[i])>menor:
            menor=len(lista[i])
            pos=i
print("La palabra mas larga es", lista[pos]," y tiene", menor,"caracteres")
   

