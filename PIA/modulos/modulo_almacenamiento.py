import openpyxl
import os
import shutil
BASE = os.path.dirname(os.path.dirname(__file__))

CARPETA_API = os.path.join(BASE, "reportes_api")
CARPETA_EXCEL = os.path.join(BASE, "reportes_excel")
CARPETA_GRAFICAS = os.path.join(BASE, "graficas")

os.makedirs(CARPETA_API, exist_ok=True)
os.makedirs(CARPETA_EXCEL, exist_ok=True)
os.makedirs(CARPETA_GRAFICAS, exist_ok=True)

def guardar_texto(albumes, nombre, numero, fecha):
    archivo = os.path.join(
        CARPETA_API,
        f"consulta{numero}_{nombre}_{fecha}.txt"
    )

    with open(archivo, "w", encoding="utf-8") as f:
        for alb in albumes:
            f.write(f"Nombre: {alb['nombre']}\n")
            f.write(f"ID: {alb['id']}\n")
            f.write(f"Fecha: {alb['fecha']}\n")
            f.write(f"Canciones: {alb['cant_pistas']}\n")
            f.write(f"Duracion: {alb['duracion']} ms\n\n")

    print(" TXT guardado:", archivo)
    
def guardar_excel(albumes, nombre, numero, fecha):
    archivo = os.path.join(
        CARPETA_EXCEL,
        f"reporte{numero}_{nombre}_{fecha}.xlsx"
    )
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Discografia " + nombre
    ws.append(["Nombre", "ID", "Fecha",
               "Canciones", "Duracion (ms)"])
    for alb in albumes:
        ws.append([
            alb["nombre"],
            alb["id"],
            alb["fecha"],
            alb["cant_pistas"],
            alb["duracion"]
        ])

    wb.save(archivo)
    print(" Excel guardado:", archivo)
def borrar_reportes():

    afirmativo = {"s", "si", "sí"}

    res = input(" ¿Borrar todo? (s/n): ")
    if res.lower() not in afirmativo:
        print(" Cancelado")
        return

    for carpeta in [CARPETA_API, CARPETA_EXCEL, CARPETA_GRAFICAS]:
        if os.path.exists(carpeta):
            shutil.rmtree(carpeta)
            os.makedirs(carpeta)

    print(" Todos los reportes fueron borrados")
