#Problema 49
resps = ["si", "SI", "Si", "sI", "S"]

n = int(input("ingrese la cantidad de productos: "))
prod = {}
for i in range(0, n):
    nom = input("indique el nombre del producto: ")
    cla = input("indique la clave del producto: ")
    exis = input("indique la cantidad de piezas en existencia: ")
    ind = i+1
    prod[ind] = [nom, cla, exis]
    
ans = 'Si'
while(ans in resps):
    op = input("ingrese:\n'buscar' para buscar un producto por indice\n'mostrar todo' para ver todos los productos\n: ")
    if op == "buscar":
        ind = int(input("¿Qué producto desea buscar? "))
        print(prod[ind])
    elif op == "mostrar todo":
        print(prod)
    ans = input("¿Desea realizar otra acción? ")
