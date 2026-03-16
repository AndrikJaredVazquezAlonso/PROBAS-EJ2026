#Problema 60
def sumatoria(*nums):
    s = 0
    for i in nums:
        s+=i
    return s
def prom(n, *nums):
    s = sumatoria(*nums)
    return s/n
    
