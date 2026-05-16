# Problema 81: Escribir sin borrar el contenido anterior
try:
    frase = input("Ingresa una frase: ")
    with open("registro.txt", "a", encoding="utf-8") as archivo:
        archivo.write(frase + "\n")
    print("Frase agregada exitosamente.")
except Exception as e:
    print(f"Error: {e}")
