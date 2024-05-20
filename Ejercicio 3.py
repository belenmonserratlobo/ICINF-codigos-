cont=0
promedio=0
sum=0
while True:
    n=float(input("Ingrese la altura: "))
    if n==0:
        promedio=sum/cont
        print("El promedio es",promedio)
        break 
    else:
        sum=sum+n
        cont=cont+1
        



    
