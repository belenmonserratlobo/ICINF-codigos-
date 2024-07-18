#Crear un programa en Python que implemente una funcion "convierte_negativos(lista)" , que reciba una lista
# con 10 numeros positivos ingresados por el usuario.La funcion debera devolver la misma lista pero con los
# numeros convertidos a negativos. En el programa principal mostrar el resutado final de la lista

def convierte_negativos(lista):
    for i in range(len(lista)):
        lista[i]= -lista[i]
    return lista
listaN=[]
for x in range(10):
    numero=int(input("Ingrese un numero a la lista: "))
    listaN.append(numero)
lista=convierte_negativos(listaN)
print(lista)