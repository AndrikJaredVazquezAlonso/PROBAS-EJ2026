#Problema 92
import re

parrafo = "Hola mundo. ¿Cómo estás? Estoy bien!"

oraciones = re.split(r'[.!?¿]+', parrafo)

for oracion in oraciones:
    if oracion.strip():
        print(oracion.strip())
