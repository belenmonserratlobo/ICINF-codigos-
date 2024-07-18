#Crear una funcion recursiva llamada "potencia(num,exp)", que reciba un numero (num) y un exponente(exp), y
#calcule su potencia en base al exponente

def potencia(num,exp):
    if exp == 0:
        return 1
    else:
        return num * potencia(num,exp -1) 
    
print(potencia(2,0))
print(potencia(2,2))
