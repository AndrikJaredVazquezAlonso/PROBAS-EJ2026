#Problema 86
import re

correo = input("Ingresa un correo electrónico: ")

# Patrón básico: letras/números + @ + letras + . + dominio
patron = r'^[a-zA-Z0-9]+@[a-zA-Z]+\.[a-zA-Z]+$'

if re.match(patron, correo):
    print("Válido")
else:
    print("Inválido")
