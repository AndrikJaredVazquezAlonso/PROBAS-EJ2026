#Problema 79
try:
    with open("perfil.txt", "w") as archivo:
        archivo.write(input("Ingrese su nombre: ") + "\n")
        archivo.write(input("Ingrese su edad: ") + "\n")
        archivo.write(input("Ingrese su carrera: "))
except PermissionError:
    print("ERROR: No tienes permisos para escribir en el archivo")
