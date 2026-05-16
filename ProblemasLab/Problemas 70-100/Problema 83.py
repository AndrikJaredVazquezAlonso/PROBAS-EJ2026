#Problema 83
try:
    numeros = []
    
    with open("numeros.txt", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            try:
                num = float(linea.strip())
                numeros.append(num)
            except ValueError:
                print(f"error, linea invalida: '{linea.strip()}'")
    
    if len(numeros) == 0:
        print("error, no hay numeros validos")
    else:
        promedio = sum(numeros) / len(numeros)
        print(f"Promedio: {promedio:.2f}")
        
except FileNotFoundError:
    print("error, archivo 'numeros.txt' no existe")
except Exception as e:
    print(f"error: {e}")
