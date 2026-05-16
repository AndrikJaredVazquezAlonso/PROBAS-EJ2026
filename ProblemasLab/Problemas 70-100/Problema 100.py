#Problema 100
import requests

url = "https://pokeapi.co/api/v2/pokemon?limit=5"
res = requests.get(url)
datos = res.json()

for pok in datos["results"]:
    print(pok["name"])
