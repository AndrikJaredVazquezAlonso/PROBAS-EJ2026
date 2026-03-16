#Problema 44: Calculadora básica con repetición
ans = 'Si'
while ans in {"Si", "si", "SI"}:
    a = float(input("ingrese el número 1: "))
    b = float(input("ingrese el número 2: "))
    op = input("¿Qué operación desea realizar?\n+ --> suma\n- --> resta\nx --> multiplicación\n/--> división\n** --> exponenciación\n% --> módulo\n: ")
    if op == "+":
        print(a+b)
    elif op == "-":
        print(a-b)
    elif op == "x":
        print(a*b)
    elif op == "/" and b!=0:
        print(a/b)
    elif op == "**" and (a!=0 or b!=0):
        print(a**b)
    elif op == "%" and b!=0:
        print(a%b)
    else:
        print("operación inválida")
    ans = input("¿Desea realizar otra operación?: ")
