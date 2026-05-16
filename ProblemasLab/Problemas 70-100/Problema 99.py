#Problema 99
import requests

while True:
    try:
        numero = int(input("ingrese un numero: "))
        break
    except ValueError:
        print("el numero debe ser entero")

url = f"https://numbersapi.com/{numero}?json"
res = requests.get(url)
try:
    datos = res.json()
    print(datos["text"])

except requests.exceptions.JSONDecodeError:
    print("No se recibieron datos")

