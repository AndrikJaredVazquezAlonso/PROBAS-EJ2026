#Problema 95
import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=19.43&longitude=-99.13&current_weather=true"

res = requests.get(url)
datos = res.json()
    
clima = datos["current_weather"]
temperatura = clima["temperature"]
viento = clima["windspeed"]
    
print(f"Temperatura actual: {temperatura} °C")
print(f"Velocidad del viento: {viento} km/h")
