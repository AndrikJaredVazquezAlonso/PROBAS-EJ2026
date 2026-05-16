#Problema 78
try:
    with open("datos.txt", "r") as archivo:
        texto= archivo.read()
        caracteres = len(texto)
        palabras = len(texto.split())
        lineas = len(texto.splitlines())
        print("Total de caracteres: ", caracteres, "\n Total de palabras: ", palabras, "\n Total de lineas: ", lineas)
except:
    print("ERROR: Archivo no encontrado")
