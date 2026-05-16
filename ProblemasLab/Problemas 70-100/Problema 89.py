#Problema 89
import re

contraseña = input("Ingresa una contraseña: ")

# Verificaciones individuales
longitud = len(contraseña) >= 8
mayuscula = re.search(r'[A-ZÁÉÍÓÚÑ]', contraseña)
minuscula = re.search(r'[a-záéíóúñ]', contraseña)
numero = re.search(r'\d', contraseña)

if longitud and mayuscula and minuscula and numero:
    print("Contraseña segura")
else:
    print("Insegura")
