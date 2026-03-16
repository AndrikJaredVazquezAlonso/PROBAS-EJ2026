#Problema 46
datos = input("indique 10 números: ")
datos = datos.split()
for i in range(0, 10):
    datos[i] = float(datos[i])
    ans = datos[i]*datos[i]
    print(ans)
