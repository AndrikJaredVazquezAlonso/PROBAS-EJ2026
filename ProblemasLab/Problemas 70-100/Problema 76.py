#Problema 76
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 8, 7]
plt.plot(x, y, marker='o')
plt.title("Grafica del problema 76")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.savefig("grafica.png")
plt.show()
