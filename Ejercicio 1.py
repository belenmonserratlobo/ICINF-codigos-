Tpreguntas=int(input("Ingrese el total de preguntas realizadas: "))
Cpreguntas=int(input("Ingrese la cantidad de preguntas respondidas correctamente: "))
porcentaje=Cpreguntas*100/Tpreguntas
if porcentaje>= 95:
    print("Nivel maximo")
else:
    if porcentaje>=70 and porcentaje<95:
        print("Nivel medio")
    else:
        if porcentaje>=40 and porcentaje<70:
            print("Nivel regular")
        else:
            if porcentaje<40:
                print("Fuera de nivel")
