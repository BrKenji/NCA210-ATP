## Ex.1
"""
lista = []
sum_aux = 0
sum_aux2 = 0

n = int(input("Digite o tamanho da lista: "))
print("Digite os valores: ")

for i in range(n):
    x = int(input())
    sum_aux += x
    lista.append(x)
m = (1/len(lista))*sum_aux

for i in range(len(lista)):
    sum_aux2 += (lista[i] - m)**2

from math import sqrt

d = sqrt((1/len(lista))*sum_aux2)

print("Média = %.1f e Desvio = %.4f" %(m, d))
"""

## Ex.2
"""
lista = []
n = int(input())
while(n != 0):
    lista.append(n)
    n = int(input())

lista_n = [x for x in lista if(x<0)]

lista_p = [x for x in lista if(x>0)]

print(*lista_n)
print(*lista_p)
"""

## Ex.3
"""
lista = []

for i in range(20):
    x = int(input())
    lista.append(x)

lista_par = [x for x in lista if(x%2 == 0)]

lista_impar = [x for x in lista if(x%2 == 1)]

print(*lista)
print(*lista_par)
print(*lista_impar)
"""

## Ex.4
"""
vetor_1 = []
vetor_2 = []
aux = 0

print("Digite o primeiro vetor: ")
for i in range(3):
    n = int(input())
    vetor_1.append(n)

print("Digite o segundo vetor: ")
for i in range(3):
    n = int(input())
    vetor_2.append(n)

for i in range(len(vetor_1)):
    aux += vetor_1[i]*vetor_2[i]

print(aux)
"""

## Ex.5
"""
temperaturas = [-4, -2, 10, 5, 11, 204, -17, 12, 20, 22, -58, 21, 19, 17, 999]

aux = 0

temperaturas_corretas = [x for x in temperaturas if(-10<=x<=100)]

aux = sum(temperaturas_corretas)

print(temperaturas)   
print(temperaturas_corretas)
print("Média igual a %.1f" %(aux/len(temperaturas_corretas)))
"""
