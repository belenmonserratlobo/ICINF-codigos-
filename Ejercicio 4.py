sum=0
cont1=0
cont2=0
while True:
    n=int(input("Ingrese el valor de su sueldo: "))
    if n==-1:
        print("La empresa gasta un total de",sum)
        break 
    else:
        sum=sum+n
    if n>=500000 and n<=900000:
        cont1=cont1+1
    else:
        n>900000
        cont2=cont2+1
print("Los empleados que cobran entre $500.000 y $900.000 son",cont1)
print("Loss empleados que cobran mas de $900.000 son",cont2)
           
        
