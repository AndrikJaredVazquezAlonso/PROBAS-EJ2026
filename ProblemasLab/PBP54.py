#Problema 54
nombre = input("ingrese los nombres: ").split()
ahorro = input("ingrese los ahorros: ").split()
n = len(nombre)
for i in range(0, n):
    ahorro[i] = float(ahorro[i])
    if ahorro[i] < 1000:
        print(f"{nombre[i]} no tendrás para tu futuro")
    elif ahorro[i] > 1000000:
        print(f"{nombre[i]} ya merito te retiras")
