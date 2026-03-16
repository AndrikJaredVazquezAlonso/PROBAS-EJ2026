#Problema 36: Repetir elevación al cuadrado
ans = 'S'
while ans == 'S':
    x = float(input("ingrese un número: "))
    x = x*x
    print(x, '\n')
    ans = input("desea ingresar otro número? S/N: ")
