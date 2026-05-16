#Problema 85
import re

# Entrada de texto
texto = input("Ingresa una cadena de texto: ")

# Expresión regular: palabras que empiezan por mayúscula
patron = r'\b[A-ZÁÉÍÓÚÑ][a-záéíóúñ]*\b'
resultado = re.findall(patron, texto)

# Imprimir lista
print(resultado)
