paises={}
for i in range(5):
    pais=input("Ingrese un pais:")
    capital=input("Ingrese la capital del pais: ")
    paises[pais]=capital

nombre=input("Ingrese nombre del turista: ")
paisP=input("Ingrese su pais de procedencia: ")
print("El turista con el nombre", nombre,"viene del pais", paisP,"y su capital es",paises[paisP])