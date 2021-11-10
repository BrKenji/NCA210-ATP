## Ex1
"""
import statistics

def analise(list):
    return sum(list)/len(list), statistics.median(list),min(list), max(list)

lista = [2, 5, 7, -2, 8]

print(analise(lista))
"""
## Ex2
"""
def maximo(a, b, imp = False):
    n = max(a, b)
    if (imp == True):
        print(n)
    return n

print(maximo(1,2))
maximo(7,20, True)
"""
## Ex3
"""
def media(a, b, c, letra):
    if (letra == "A"):
        return (a + b + c)/3
    if (letra == "P"):
        return (5*a + 3*b + 2*c)/10

print(media(2,3,4,'A'))
print(media(5,4,6,'P'))
"""
## Ex4
"""
def multiplo(x, y):
    if (x%y == 0):
        return True
    else:
        return False

print(multiplo(10,5))
"""
## Ex5
"""
def produtorio(*args):
    aux = 1
    for arg in args:
        aux*=arg
    return aux

print(produtorio(2, 2, 2))
print(produtorio(2, 4, 2, 2))
"""
