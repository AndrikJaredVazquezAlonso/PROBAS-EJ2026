#Problema 90. Censurar palabras
import re
texto = "Eres muy tonto y FEo conmigo."
palabras_prohibidas = ["tonto", "feo"]

patron = "|".join(palabras_prohibidas)

def censurar(match):
    return "*" * len(match.group())

texto_censurado = re.sub(patron, censurar, texto, flags=re.IGNORECASE)
print("Texto censurado:")
print(texto_censurado)
