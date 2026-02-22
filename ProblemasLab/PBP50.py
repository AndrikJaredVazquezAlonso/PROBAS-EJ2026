#Problema 50
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
    op1 = input("ingrese:\n'buscar' para buscar un producto por indice\n'mostrar todo' para ver todos los productos\n: ")
    if op1 == "buscar":
        op2 = input("ingrese:\n'indice' para buscar por indice\n'nombre' para buscar por nombre\n'clave'para buscar por clave\n: ")
        term = False
        if op2 == 'indice':
            ind = int(input("ingrese el indice del producto "))
            if ind>0 and ind<=n: print(prod[ind])
            else: print("No encontrado")
        elif op2 == 'nombre':
            nom = input("indique el nombre del producto: ")
            for k in prod:
                for e in prod[k]:
                    if e == nom:
                        print(prod[k])
                        term = True
            if term == False: print("No encontrado")
        elif op2 == 'clave':
            cla = input("indique la clave del producto: ")
            for k in prod:
                for e in prod[k]:
                    if e == cla: print(prod[k])
            if term == False: print("No encontrado")
    elif op1 == "mostrar todo":
        print(prod)
    ans = input("¿Desea realizar otra acción? ")
