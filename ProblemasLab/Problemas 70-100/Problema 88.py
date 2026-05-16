#Problema 88
import re

texto = input("Ingresa el texto donde buscar fechas: ")

# Patrón: días 1-31, meses 1-12, años de 4 dígitos
patron = r'\b(0?[1-9]|[12]\d|3[01])/(0?[1-9]|1[012])/\d{4}\b'
fechas = re.findall(patron, texto)

# Reconstruir fechas completas
fechas_completas = [f"{d}/{m}/{a}" for d, m, a in re.findall(r'\b(\d{1,2})/(\d{1,2})/(\d{4})\b', texto)]
print(fechas_completas)
