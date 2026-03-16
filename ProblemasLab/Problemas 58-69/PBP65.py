#Problema 65
ans = ["SI","Si","sI","si","s","S"]
def fac(n):
    if n==0: return 1
    else: return n*fac(n-1)
stop = "si"
cont = 0
while stop in ans:
    num = int(input("ingresa un número entero: "))
    print(fac(num))
    cont+=1
    stop = input("¿Quieres introducir otro número? ")
print(cont)
