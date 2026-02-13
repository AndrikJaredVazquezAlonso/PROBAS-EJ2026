#Problema 37: Interés compuesto con repetición
ans = 'S'
while ans == 'S':
    c = float(input("ingrese la capital inicial: "))
    i = float(input("ingrese la tasa de interés: "))
    n = int(input("ingrese el número de períodos: "))
    m = c*(1+i)**n
    print(m)
    ans = input("desea hacer otro cálculo?: ")
