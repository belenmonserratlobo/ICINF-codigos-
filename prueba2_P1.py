notas=[]
cont=0
while True:
    nota=float(input("Ingrese una nota: "))
    if nota == 0:
        break
    notas.append(nota)
print(notas)

for i in notas:
    cont+=1
print("La cantidad de notas ingresadas es:", cont)
sum=0
for i in notas: 
    sum=sum+i
print("El promedio de las notas es:", sum/cont)


notas.sort

print("La nota maxima es",notas[0])
print("La nota minima es",notas[-1] )
