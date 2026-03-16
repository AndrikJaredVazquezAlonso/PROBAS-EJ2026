#Problema 67
#Lista de prueba
l = [1,2,3,4,4,3,2,-1,-5,8,10,-30,5,2,1]
def ordencre(lista):
    n = len(lista)
    for i in range (1,n):
        for j in range(1,n):
            if lista[j]<lista[j-1]:
                aux = lista[j-1]
                lista[j-1] = lista[j]
                lista[j] = aux
    return lista

def ordendec(lista):
    n = len(lista)
    for i in range (1,n):
        for j in range(1,n):
            if lista[j]>lista[j-1]:
                aux = lista[j-1]
                lista[j-1] = lista[j]
                lista[j] = aux
    return lista

def delind(lista,ind):
    n = len(lista)
    newlis = []
    for i in range(0,n):
        if i!=ind: newlis.append(lista[i])
    return lista[ind]

def deldat(lista, dat):
    delet = False
    newlis = []
    for i in lista:
        if i!=dat: newlis.append(i)
        else:
            if delet: newlis.append(i)
            else: delet = True
    return newlis

def promaxmin(lista):
    s = 0
    low = 1e9
    high = -1e9
    for i in lista:
        s+=i
        if i<low: low=i
        if i>high: high=i
    return s/len(lista), high, low
