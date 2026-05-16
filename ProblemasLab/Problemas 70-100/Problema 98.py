#Problema 98
import requests

url = "https://api.dictionaryapi.dev/api/v2/entries/en/example"
res = requests.get(url)
datos = res.json()

palabra = datos[0]["word"]
definicion = datos[0]["meanings"][0]["definitions"][0]["definition"]

print(f"{palabra}: {definicion}")
