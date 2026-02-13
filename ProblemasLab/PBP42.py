#Problema 42: Confirmación de contraseña (con límite)
pswrd = input("ingrese su contraseña: ")
conpswrd = ""
i=0
while conpswrd != pswrd and i<3:
    conpswrd = input("confirme su contraseña: ")
    i+=1
if pswrd != conpswrd:
    print("Cuenta cancelada")
