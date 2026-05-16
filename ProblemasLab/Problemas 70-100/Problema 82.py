# Problema 82: Combinar archivos de texto
try:
    with open("a.txt", "r", encoding="utf-8") as a, \
         open("b.txt", "r", encoding="utf-8") as b:
        
        contenido_a = a.read()
        contenido_b = b.read()
        
    with open("combinado.txt", "w", encoding="utf-8") as combinado:
        combinado.write(contenido_a + contenido_b)
        
    print("Archivos combinados en 'combinado.txt'")
    
except FileNotFoundError as e:
    print(f"Error: No se encontró el archivo {e.filename}")
except Exception as e:
    print(f"Error: {e}")
