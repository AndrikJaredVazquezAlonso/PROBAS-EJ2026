#Problema 77
try:
    with open("entrada.txt", "r") as archivo:
        for num, linea in enumerate (archivo, start=1):
            print(num, ".-", linea.strip())
except FileNotFoundError:
    print("ERROR: El archivo no existe")
