#Problema 75
import sys
from pathlib import Path
if len(sys.argv) == 3:
    archivo= Path(sys.argv[1])
    n= sys.argv[2]
    try:
        n = int(sys.argv[2])
    except (ValueError, IndexError):
        print("Error: El segundo argumento debe ser un número entero.")
        sys.exit(1)
    if archivo.exists() and archivo.is_file():           
        with open(archivo, "r") as txt:
            for x in range(n):
                print((txt.readline()).strip())
    else:
        print("El archivo no existe")
else:
    print("Cantidad de argumentos invalida")
