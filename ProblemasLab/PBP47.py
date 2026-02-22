#Problema 47
n = int(input("indique de cuántas materias va a capturar calificaciones: "))
calif = {}
for i in range(0, n):
    nombre = input("ingrese el nombre de la materia: ")
    suma = 0
    for j in range (0, n):
        inpt = float(input(f"ingrese la calificación {j}: "))
        suma += inpt
    if n>0: calif[nombre] = suma/n
    else: calif[nombre] = 0
for i in calif:
    print(i, calif[i])
