#Crear un programa en python que implemente una funcion "solo_numeros(var)", que devuelva un True si un 
#string contiene solo numeros, de lo contrario un False

def solo_numeros(var):
    try:
        float(var)
        return True
    except:
        return False
    
print(solo_numeros("hola"))
print(solo_numeros(12))
print(solo_numeros(1.5))
