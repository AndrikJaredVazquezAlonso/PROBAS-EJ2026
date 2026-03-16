#Problema 69
def isemail(mail):
    hasat = False
    for i in mail:
        if i=='@': hasat = True
    return hasat
email = input("ingrese su correo electrónico: ")
if(isemail(email)): print("Es válida")
else: print("No es válida")
