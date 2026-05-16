#Problema 87
import re

texto = input("Ingresa una cadena de texto: ")

# Patrón: números como 123, 4.56, .78, 0.9
patron = r'\d+\.\d*|\.\d+|\d+'
encontrados = re.findall(patron, texto)

# Convertir a float
numeros = [float(num) for num in encontrados]
print(numeros)
