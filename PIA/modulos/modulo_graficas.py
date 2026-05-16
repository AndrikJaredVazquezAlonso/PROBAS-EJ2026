import matplotlib.pyplot as plt
import openpyxl as xl
import os

os.makedirs("reportes_excel", exist_ok=True)
os.makedirs("graficas", exist_ok=True)

def genera_graficas(archivo,nombre,numero, fecha):

    wb = xl.load_workbook(archivo)
    ws = wb.active
    nombres_discos = []
    fechas = []
    total_canciones = []
    duracion = []
    
    for fila in ws.iter_rows(min_row=2, values_only=True):
        
        if fila[3]>=4: #tiene que tener por lo menos 4 canciones para ser album
            
            ndisco = fila[0]
            if len(ndisco)>32:
                
                nombres_discos.append(ndisco[0:31]+"...")
                
            else:
                
                nombres_discos.append(ndisco)
                
            fechas.append(fila[2])
            total_canciones.append(fila[3])
            duracion.append(fila[4])
        
    plt.figure(figsize=(12, 8))
    plt.bar(nombres_discos,total_canciones, color="green")

    titulo = "¿Cuantas canciones tiene por album " + nombre + "?"
    plt.title(titulo)
    plt.xlabel('Disco')
    plt.ylabel('Total de canciones')
    plt.xticks(rotation=72)
    plt.rcParams['axes.edgecolor'] = 'black'
    plt.tight_layout()
    
    grafica1 = "graficas/grafica" + str(numero) + "_" + nombre + "_1_" + fecha + ".png"
    
    plt.savefig(grafica1)
    plt.show()
    plt.close()
    mensaje = " Grafica 1 guardada: " + grafica1
    print(mensaje)

    fig, ax = plt.subplots(figsize=(12, 8))
    ax.pie(duracion, labels=nombres_discos, autopct='%1.1f%%', shadow=True)

    titulo = "Duracion de cada album en la discografia de " + nombre
    plt.title(titulo)
    plt.rcParams['axes.edgecolor'] = 'black'
    plt.tight_layout()

    grafica2 = "graficas/grafica" + str(numero) + "_" + nombre + "_2_" + fecha + ".png"

    plt.savefig(grafica2)
    plt.show()
    plt.close()
    mensaje = " Grafica 2 guardada: " + grafica2
    print(mensaje)

    
    promedio_cancion = []
    
    for i in range(0,len(total_canciones)):
        
        promedio_cancion.append(duracion[i]/total_canciones[i])
        
    plt.figure(figsize=(12, 8))
    plt.plot(nombres_discos, promedio_cancion, marker='*', color='green')
    plt.xticks(rotation=72)
    plt.xlabel("Album")
    plt.ylabel("Promedio (en ms)")

    titulo = "Promedio de duracion de cada cancion por album de " + nombre
    plt.title(titulo)
    plt.rcParams['axes.edgecolor'] = 'black'
    plt.tight_layout()

    grafica3 = "graficas/grafica" + str(numero) + "_" + nombre + "_3_" + fecha +".png"
    plt.savefig(grafica3)
    plt.show()
    plt.close()
    mensaje = " Grafica 3 guardada: " + grafica3
    print(mensaje)
