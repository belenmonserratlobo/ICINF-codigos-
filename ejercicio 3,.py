supermercado={}
while True: 
   producto=input("Ingrese el nombre del producto(enter para finalizar): ")
   if producto=="":
    break
   cantidad=int(input("Ingrese la cantidad del producto: "))
   supermercado[producto]= cantidad
X=int(input("Ingrese un valor numero: "))

for producto, cantidad in supermercado.items():
    print(producto, ":", cantidad*X)
