#Problema 55
resps = {"si", "sI", "Si", "SI"}
ans = "si"
op1 = input("ingrese:\n'numeros' para crear una lista de números\n'texto' para crear una lista de texto\n: ")
if op1 == "numeros":
    lista = input("ingrese la lista: ").split()
    n = len(lista)
    for i in range(0, n):
        lista[i] = float(lista[i])
    while ans in resps:
        op2 = input("ingrese\n'agregar' para agregar un número a la lista\n'eliminar' para eliminar valores de la lista\n'ordenar directo' para ordenar la lista modificandola directamente\n'ordenar copia' para crear una nueva lista ordenada\n'buscar' para encontrar un valor especifico y mostrar el indice\n'maximo' para encontrar el valor máximo\n'minimo' para encontrar el valor mínimo\n'suma' para calcular la suma\n'promedio' para calcular el promedio\n: ")
        if op2 == "agregar":
            inpt = float(input("ingrese un número: "))
            lista.append(inpt)
            print(lista)
        elif op2 == "eliminar":
            inpt = float(input("ingrese el número a elininar: "))
            lista.remove(inpt)
            print(lista)
        elif op2 == "ordenar directo":
            lista.sort()
            print(lista)
        elif op2 == "ordenar copia":
            lista2 = lista
            lista2.sort()
            print(lista, "\n", lista2)
        elif op2 == "buscar":
            inpt = float(input("ingrese el elemento a buscar: "))
            ind = lista.index(inpt)
            print(ind)
        elif op2 == "maximo":
            print(max(lista))
        elif op2 == "minimo":
            print(min(lista))
        elif op2 == "suma":
            print(sum(lista))
        elif op2 == "promedio":
            s = sum(lista)
            n = len(lista)
            if n != 0: print(s/n)
            else: print(0)
        else: print("instrucción inválida")
        ans = input("desea realizar otra acción?: ")
elif op1 == "texto":
    lista = input("ingrese la lista").split()
    while ans in resps:
        op2 = input("ingrese\n'agregar' para agregar un texto a la lista\n'eliminar' para eliminar valores de la lista\n'ordenar directo' para ordenar la lista modificandola directamente\n'ordenar copia' para crear una nueva lista ordenada\n'buscar' para encontrar un valor especifico y mostrar el indice\n: ")
        if op2 == "agregar":
            inpt = input("ingrese un texto: ")
            lista.append(inpt)
            print(lista)
        elif op2 == "eliminar":
            inpt = input("ingrese el texto a elininar: ")
            lista.remove(inpt)
            print(lista)
        elif op2 == "ordenar directo":
            lista.sort()
            print(lista)
        elif op2 == "ordenar copia":
            lista2 = lista
            lista2.sort()
            print(lista, "\n", lista2)
        elif op2 == "buscar":
            inpt = input("ingrese el elemento a buscar: ")
            ind = lista.index(inpt)
            print(ind)
        else: print("instrucción inválida")
        ans = input("desea realizar otra acción?: ")
        
