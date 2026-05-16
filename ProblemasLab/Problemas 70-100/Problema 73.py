#Problema 73
import numpy as np
from scipy.integrate import quad

# Definimos la función f(x) = sin(x^2)
def funcion(x):
    return np.sin(x**2)

# Calculamos la integral de 0 a 2
resultado, error = quad(funcion, 0, 2)

print(f"El valor de la integral de sin(x^2) en [0, 2] es: {resultado:.6f}")
