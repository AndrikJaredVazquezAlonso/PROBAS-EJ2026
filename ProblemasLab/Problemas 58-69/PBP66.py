#Problema 66
def reprobados(alumno, calificacion):
    n = len(alumno)
    malos = []
    for i in range(0,n):
        if calificacion[i]<70: malos.append(alumno[i])
    return malos
