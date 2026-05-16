#Problema 72
import pandas as pd

data = {
    "Producto": ["bimbo", "alpura", "suavitel", "pachoncito"],
    "Precio": [45, 27, 72, 103],
    "Cantidad": [400, 350, 273, 321]
}

df = pd.DataFrame(data)

print("--- DataFrame Creado ---")
print(df)
print("\n--- Estadísticas Principales ---")
print(df.describe()) # Muestra media, desviación estándar, min, max, etc.
