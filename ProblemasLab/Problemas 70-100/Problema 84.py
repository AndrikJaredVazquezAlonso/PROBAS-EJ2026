#Problema 84
nombre_archivo = input("Nombre del archivo: ")

try:
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        contenido = archivo.read(5)
        
        if len(contenido) < 5:
            print("error, el archivo tiene menos de 5 caracteres")
        else:
            numero = int(contenido)
            print(f"Numero: {numero}")
            
except FileNotFoundError:
    print("error, ese archivo no existe")
except ValueError:
    print("error, contenido que no es numero entero")
except Exception as e:
    print(f"error: {e}")
