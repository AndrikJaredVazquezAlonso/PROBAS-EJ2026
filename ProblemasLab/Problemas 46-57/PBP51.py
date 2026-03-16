#Problema 51
nombre = input("ingrese los nombre de los trabajadores: ").split()
asis = input("indique con '1' si asistió y '0' si no asistió: ").split()
n = len(nombre)
for i in range(0, n):
    if asis[i] == '0':
        print(nombre[i], "no asistió")
    else:
        print(nombre[i], "asistió")
