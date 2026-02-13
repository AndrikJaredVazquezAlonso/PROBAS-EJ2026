#Problema 41: Confirmación de contraseña (sin límite)
pswrd = input("ingrese su contraseña: ")
conpswrd = ""
while conpswrd != pswrd:
    conpswrd = input("confirme su contraseña: ")
