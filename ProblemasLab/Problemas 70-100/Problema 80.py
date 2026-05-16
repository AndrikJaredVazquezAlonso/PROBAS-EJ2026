# Problema 80: Copiar el contenido de un archivo a otro
try:
    with open("origen.txt", "r", encoding="utf-8") as archivo_origen:
        contenido = archivo_origen.read()
    
    with open("copia.txt", "w", encoding="utf-8") as archivo_copia:
        archivo_copia.write(contenido)
    
    print("El archivo 'copia.txt' fue creado con el contenido de 'origen.txt' exitosamente")
    
except FileNotFoundError:
    print("Error, el archivo 'origen.txt' no existe.")
except Exception as e:
    print(f"Error inesperado: {e}")
