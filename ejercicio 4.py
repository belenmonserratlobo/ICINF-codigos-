deudores = {}


for i in range(5):
    rut = input("Ingresa el RUT del deudor: ")
    deuda = float(input("Ingresa la deuda en pesos: "))
    deudores[rut] = deuda

while True:
    rut_abono = input("Ingresa el RUT del deudor para realizar un abono (o presiona Enter para finalizar): ")
    if rut_abono == "":
        break
    abono = float(input("Ingresa el monto del abono en pesos: "))
    
    if rut_abono in deudores:
        deudores[rut_abono] -= abono
        
        if deudores[rut_abono] == 0:
            del deudores[rut_abono]


print("Deudores restantes:")
for rut, deuda in deudores.items():
    print(f"RUT: {rut}, Saldo de deuda: {deuda} pesos")
