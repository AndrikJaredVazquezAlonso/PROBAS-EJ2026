#Problema 53
reps = {"si", "sI", "Si", "SI"}
ans = "si"
datos = []
while ans in reps:
    dato = int(input("ingrese un número: "))
    datos.append(dato)
    ans = input("¿Desea agregar otro número? ")
datos.sort()
print(datos)
