#Problema 48
resps = ["si", "SI", "Si", "sI", "S"]
n = int(input("ingrese la cantidad de productos: "))
nombre = [0]
clave = [0]
existen = [0]
for i in range(0, n):
    nom = input("indique el nombre del producto: ")
    cla = input("indique la clave del producto: ")
    exis = input("indique la cantidad de piezas en existencia: ")
    nombre.append(nom)
    clave.append(cla)
    existen.append(exis)
ans = 'Si'
while(ans in resps):
    ind = int(input("¿Qué producto desea buscar? "))
    print(nombre[ind], clave[ind], existen[ind])
    ans = input("¿Desea buscar otro producto?")

