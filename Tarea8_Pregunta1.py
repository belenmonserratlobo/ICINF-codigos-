"""
Crear una función llamada area_rectangulo(base, altura) que devuelva
el área del rectángulo (con return) a partir de una base y una altura.
Calcular el área de un rectángulo utilizando la función a crear para un
rectángulo de 15 de base y 10 de altura.
Obs.: El área de un rectángulo se obtiene al multiplicar la base por la
altura.
"""
def area_rectangulo(base,altura):
    area=base*altura
    return area
print(f"La area de un rectangulo de base 15 y altura 10 es: {area_rectangulo(15,10)}")