#Problema 68
def isprime(n):
    if n<2: return False
    isp = True
    for i in range(2, n):
        if n%i==0: isp=False
    return isp
