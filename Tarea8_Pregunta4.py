"""
Crear una función recursiva sumatoria(numero) que permita calcular la
sumatoria de un número y devuelva su resultado (con return).
"""
def sumatoria(numero):
    if numero==0:
        return 0
    else:
        return numero + sumatoria(numero-1)
    
print(sumatoria(1))