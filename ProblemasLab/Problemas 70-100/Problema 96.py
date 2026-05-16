#Problema 96
import requests

url = "https://pokeapi.co/api/v2/pokemon/25"
res = requests.get(url)
datos = res.json()

nombre = datos["forms"][0]["name"]
tipos = datos["types"][0]["type"]["name"]

print(f"El nombre del pokemón es {nombre}")
print(f"El tipo del pokemón es {tipos}")
