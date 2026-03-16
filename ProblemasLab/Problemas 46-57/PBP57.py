palabra = input("Ingrese la palabra a buscar")

palabras = ["pan","therians","coca cola", "epstein", \
            "furros", "FIME", "Bisonte", "Integral" , \
            "tiempo", "tigres"]

v = palabras.count(palabra)

if v != 0:
    print("Si esta en la lista")
else:
    print("No esta en la lista")
