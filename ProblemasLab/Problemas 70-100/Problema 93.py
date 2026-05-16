#Problema 93
import requests

url = "http://numbersapi.com/42?json"

response = requests.get(url)

try:
    datos = response.json()
    print(datos["text"])

except Exception as e:
    print("Error:")
    print(e)

    print("\nRespuesta real:")
    print(response.text)
    
