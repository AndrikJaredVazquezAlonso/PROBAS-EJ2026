#Problema 43: Acumulador de abonos
suma = 0.0
while suma < 100000.0:
    x = float(input("¿Cantidad a abonar? "))
    if x<0:
        print("No puede abonar cantidades negativas")
    else:
        suma = suma + x
