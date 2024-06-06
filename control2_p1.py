dias=[]
puntos=[]
for x in range (15):
    dia=int(input("Ingrese el dia del curso: "))
    dias.append(dia)
    punto=int(input("Ingrese sus puntos del dias: "))
    puntos.append(punto)

for x in range(15):
    if puntos[x]>= 60:
        print("EL dia", dias[x],"tuvo mas o igual a 60 puntos")
    elif puntos[x]<60:
        print("El dia", dias[x],"tuvo menos a 60 puntos")