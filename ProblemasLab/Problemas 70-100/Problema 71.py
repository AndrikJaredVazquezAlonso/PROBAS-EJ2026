#Problema 71
import sympy as sp

x = sp.symbols('x')

# a) x^2 - 5x + 7 = 0
eq1 = x**2 - 5*x + 7
solucion_a = sp.solve(eq1, x)
print(f"a) Soluciones de x^2 - 5x + 7: {solucion_a}")

# b) 7x^2 + 9x - 7 = 8x^2 - 2x - 3
# Igualamos a cero pasando todo a un lado: (7x^2... ) - (8x^2...) = 0
eq2 = sp.Eq(7*x**2 + 9*x - 7, 8*x**2 - 2*x - 3)
solucion_b = sp.solve(eq2, x)
print(f"b) Soluciones de la ecuación: {solucion_b}")
