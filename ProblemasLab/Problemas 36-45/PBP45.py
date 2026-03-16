#Problema 45: Calculadora con repetición por operación
ans = 'Si'
while ans in {"Si", "si", "SI"}:
    a = float(input("ingrese el número 1: "))
    b = float(input("ingrese el número 2: "))
    op = input("¿Qué operación desea realizar?\n+ --> suma\n- --> resta\nx --> multiplicación\n/--> división\n** --> exponenciación\n% --> módulo\n: ")
    if op == "+":
        print(a+b)
        con = input("¿Desea repetir la misma operación? ")
        while con in {"Si", "si", "SI"}:
            a = float(input("ingrese el número 1: "))
            b = float(input("ingrese el número 2: "))
            print(a+b)
            con = input("¿Desea repetir la misma operación? ")
    elif op == "-":
        print(a-b)
        con = input("¿Desea repetir la misma operación? ")
        while con in {"Si", "si", "SI"}:
            a = float(input("ingrese el número 1: "))
            b = float(input("ingrese el número 2: "))
            print(a-b)
            con = input("¿Desea repetir la misma operación? ")
    elif op == "x":
        print(a*b)
        con = input("¿Desea repetir la misma operación? ")
        while con in {"Si", "si", "SI"}:
            a = float(input("ingrese el número 1: "))
            b = float(input("ingrese el número 2: "))
            print(a*b)
            con = input("¿Desea repetir la misma operación? ")
    elif op == "/" and b!=0:
        print(a/b)
        con = input("¿Desea repetir la misma operación? ")
        while con in {"Si", "si", "SI"}:
            a = float(input("ingrese el número 1: "))
            b = float(input("ingrese el número 2: "))
            if b != 0: print(a/b)
            else: print("operación inválida")
            con = input("¿Desea repetir la misma operación? ")
    elif op == "**" and (a!=0 or b!=0):
        print(a**b)
        con = input("¿Desea repetir la misma operación? ")
        while con in {"Si", "si", "SI"}:
            a = float(input("ingrese el número 1: "))
            b = float(input("ingrese el número 2: "))
            if a!=0 or b!=0: print(a**b)
            else: print("operación inválida")
            con = input("¿Desea repetir la misma operación? ")
    elif op == "%" and b!=0:
        print(a%b)
        con = input("¿Desea repetir la misma operación? ")
        while con in {"Si", "si", "SI"}:
            a = float(input("ingrese el número 1: "))
            b = float(input("ingrese el número 2: "))
            if b != 0: print(a%b)
            else: print("operación inválida")
            con = input("¿Desea repetir la misma operación? ")
    else:
        print("operación inválida")
    ans = input("¿Desea realizar otra operación distinta?: ")
