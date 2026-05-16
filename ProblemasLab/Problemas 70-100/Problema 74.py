#Problema 74
import os

def listar_csv():
    ruta = input("Introduce el nombre o ruta de la carpeta: ")

    # Validar si la carpeta existe
    if os.path.isdir(ruta):
        # Obtener archivos y filtrar por extensión .csv
        archivos = [f for f in os.listdir(ruta) if f.lower().endswith('.csv')]
        
        # Ordenar alfabéticamente
        archivos.sort()
        
        if archivos:
            print(f"\nArchivos .csv encontrados en '{ruta}':")
            for archivo in archivos:
                print(f"- {archivo}")
        else:
            print("No se encontraron archivos .csv en esta carpeta.")
    else:
        print("Error: La carpeta no existe.")

listar_csv()
