import modulos as m
import os
from PIL import Image
from datetime import datetime

def menu():

    afirmativo = {"s","S","si","sI","Si","SI","sí","sÍ","Sí","SÍ"}

    base = os.path.dirname(__file__)

    ruta_api = base + "\\reportes_api"

    if not os.path.exists(ruta_api):
        os.makedirs(ruta_api)

    archivos = os.listdir(ruta_api)
    numero_consultas = 0

    for f in archivos:
        if os.path.isfile(os.path.join(ruta_api, f)):
            numero_consultas += 1

    while True:
        print("\n -------- MENU SPOTIFY ---------\n")
        print("--> 1 Buscar discografia de artista")
        print("--> 2 Consultar reportes")
        print("--> 3 Mostrar estadisticas de reporte")
        print("--> 4 Consultar graficas")
        print("--> 5 Borrar reportes")
        print("--> 6 Salir\n")

        opcion = input(" Elige una opcion: ")

        if opcion == "1":

            fecha = datetime.now().strftime("%Y%m%d_%H%M%S")
            nombre = input(" ¿Que artista quieres buscar?: ").title()

            discografia = m.api.buscar_artista(nombre)

            if not discografia:
                print(" No se pudieron obtener datos")
                continue

            print("\n ----- Discografia encontrada -----")
            for album in discografia:
                print("Disco:", album["nombre"], "(", album["fecha"], ")", album["duracion"], "ms")

            numero_consultas += 1

            m.alm.guardar_texto(discografia, nombre, numero_consultas, fecha)
            m.alm.guardar_excel(discografia, nombre, numero_consultas, fecha)

            archivo_excel = base + "\\reportes_excel\\reporte" + str(numero_consultas) + "_" + nombre + "_" + fecha + ".xlsx"

            m.graf.genera_graficas(archivo_excel, nombre, numero_consultas, fecha)

    
        elif opcion == "2":

            while True:
                ruta = base + "\\reportes_api"
                reportes = os.listdir(ruta)

                print("\n Reportes disponibles:")
                for i in range(len(reportes)):
                    print(" -->", i+1, "  ", reportes[i])

                op = input(" Ingresa el numero de reportes: ")

                try:
                    num = int(op) - 1

                    if num < 0 or num >= len(reportes):
                        print(" ERROR: Respuesta fuera de rango")
                        continue

                    archivo = ruta + "\\" + reportes[num]

                    with open(archivo, "r") as f:
                        for linea in f:
                            print(linea, end="")

                    otro = input("\n ¿Quieres consultar otro reporte? (s/n): ")
                    if otro not in afirmativo:
                        break

                except:
                    print(" ERROR: Opcion no valida")
                    break

        elif opcion == "3":

            while True:
                ruta = base + "\\reportes_excel"
                reportes = os.listdir(ruta)

                print("\n Reportes disponibles:")
                for i in range(len(reportes)):
                    print(" -->",i+1, "  ", reportes[i])

                op = input(" Ingresa el numero de reporte: ")

                try:
                    num = int(op) - 1

                    if num < 0 or num >= len(reportes):
                        print(" ERROR: Respuesta fuera de rango")
                        continue

                    archivo = ruta + "\\" + reportes[num]

                    print("\n\t ¿Que medida quieres calcular?")
                    print("\t--> a Media de duracion de album")
                    print("\t--> b Varianza de la duracion de album")
                    print("\t--> c Porcentaje de duracion de cada album con respecto a la discografia")
                    print("\t--> d Media de total de pistas por album")
                    print("\t--> s Salir del menu")

                    op2 = input(" Ingresa una opcion: ")

                    if op2 == "a":
                        print("\t La media de duracion es:",m.calc.media_duracion(archivo))
                    elif op2 == "b":
                        print("\t La varianza de duracion es:",m.calc.varianza_discos(archivo))
                    elif op2 == "c":
                        m.calc.porcentaje_duracion(archivo)
                    elif op2 == "d":
                        print("\t La media de canciones es:",m.calc.media_pistas(archivo))
                    elif op2 == "s":
                        break

                except:
                    print(" ERROR: Opcion no valida")
                    break
        elif opcion == "4":

            while True: 
                ruta = base + "\\graficas"
                graficas = os.listdir(ruta)

                print("\n Graficas disponibles:")
                for i in range(len(graficas)):
                    print(" -->",i+1, "  ", graficas[i])

                op = input(" Ingresa el numero de grafica: ")

                try:
                    num = int(op) - 1

                    if num < 0 or num >= len(graficas):
                        print(" ERROR: Respuesta fuera de rango")
                        continue

                    img = Image.open(ruta + "\\" + graficas[num])
                    img.show()

                    otro = input(" ¿Quieres consultar otra grafica? (s/n): ")
                    if otro not in afirmativo:
                        break

                except:
                    print(" ERROR: Opcion no valida")
                    break
        elif opcion == "5":
            m.alm.borrar_reportes()
            numero_consultas = 0
            print(" Todos los reportes han sido borrados")

 
        elif opcion == "6":
            salir = input(" ¿Seguro que quieres salir? (s/n): ")
            if salir in afirmativo:
                break

        else:
            print(" ERROR: Opcion no valida")


if __name__ == "__main__":
    menu()
