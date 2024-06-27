precios=[]
precios_nuevos=[]
for i in range(10):
    precio=int(input("Ingrese un precio en dolares: "))
    precios.append(precio)
for i in precios:
    mul=0
    mul=i*950
    precios_nuevos.append(mul) 
print(precios_nuevos)