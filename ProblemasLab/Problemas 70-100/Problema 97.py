#Problema 97
import requests
import json

url = "https://api.github.com/users/google"
res = requests.get(url)
datos = res.json()

with open("respuesta.json","w",encoding="UTF-8") as f:
    json.dump(datos,f,indent=4)
