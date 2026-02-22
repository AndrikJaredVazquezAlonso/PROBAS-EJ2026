#Problema 52
prod = {"pinol": [10, 201], "milc": [20, 789], "soda pop": [25, 42], "martinez": [1, 123491], "tijerina": [41233, 2]}
for i in prod:
    ingreso = prod[i][0]*prod[i][1]
    prod[i].append(ingreso)
    print(i, prod[i])
