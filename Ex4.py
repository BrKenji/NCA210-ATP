## Ex1
"""
import random as r

matriz = []

matriz_t = []
for i in range(5):
    linha = []
    for j in range(5):
        linha.append(r.randint(0,30))
    matriz.append(linha)

for i in range(len(matriz)):
    linha = []
    for j in range(len(matriz)):
        linha.append(matriz[j][i])
    matriz_t.append(linha)

print(matriz)
print(matriz_t)
"""
## Ex2
"""
n = int(input("Digite o tamanho da matriz: "))

matriz = []
x = 1
sum_aux = 0

for i in range(n):
    linha = []
    for j in range(n):
        linha.append(x)
        if(j == i):
            sum_aux+=x
        x+=1
    matriz.append(linha)

print(matriz)
print(sum_aux)
"""
## Ex3
"""
def Linha(matriz, n): # essa função recebe uma matriz e um inteiro n e retorna uma lista que contem os elementos contidos em matriz[n]
    return [x for x in matriz[n]] 
    # exemplo: Linha(A, 1) retorna uma lista com o termo 1 da matriz A, ou seja,
    # retorna [A[1]] que é a linha 1 de A

def Coluna(matriz, n): # essa função retorna uma lista com os elementos n de cada elemento da matriz 
    return [x[n] for x in matriz]
    # exemplo: Coluna(B, 0) retorna uma lista com todos os com index 0 de cada lista da matriz, ou seja,
    # retorna [B[0][0], B[1][0], B[2][0]], que são os elementos da coluna de B

# ambas funções retornam uma matriz 1x3

A = [[1,2,3],[4,5,6],[7,8,9]]
B = []
AB = []
for i in range(len(A)):
    linha = []
    for j in range(len(A[i])):
        n = int(input())
        linha.append(n)
    B.append(linha)

for i in range(len(A)):
    AB.append([])
    for j in range(len(A[i])):
        # zip() recebe elementos iteráveis como argumentos e retorna um iterador, nesse caso, recebe duas listas e retorna uma que contém todos os elementos de mesmo index agrupados
        # Exemplo:
        # Linha(A,0) retorna [A[0][0], A[0][1], A[0][2]] = [1,2,3]
        # Coluna(B,2) retorna [B[0][2], B[1][2], B[2][2]] = [12,15,18]
        # zip(Linha(A, 0), Coluna(B, 2)) => [[1,12], [2,15], [3,18]] 
        linhaMult = [x*y for x,y in zip(Linha(A, i), Coluna(B, j))] # faz a multiplicação de x e y do resultado de zip() 
        AB[i].append(sum(linhaMult))

print(A)
print(B)
print(AB)
"""
## Ex4
"""
import random as r

seed = 100
r.seed(seed)
notas = []

# preenche a matriz notas
for i in range(10):
    linha = []
    for j in range(3):
        linha.append(r.randint(0,10))
    notas.append(linha)

# Printa bunitin a matriz notas
for i in range(len(notas)):
    for j in range(len(notas[i])):
        print("%2d "% notas[i][j], end="")
    print()

for i in range(len(notas)):
    menor_1 = 10 # maior nota possível é 10
    for j in range(len(notas[i])):
        if(notas[i][j] < menor_1):
            menor_1 = notas[i][j]
            numero_prova = j
    print("Aluno %i: Menor nota na prova %i com nota %i" %(i+1,numero_prova + 1,menor_1))

nota_1 = [x[0] for x in notas]
nota_2 = [x[1] for x in notas]
nota_3 = [x[2] for x in notas]

def getMenorNota(matriz):
    menor_nota = matriz[0]
    for i in matriz:
        if(i < menor_nota):
            menor_nota = i
    return menor_nota

print("%i alunos ficaram com %i na prova 1" %(nota_1.count(getMenorNota(nota_1)) ,getMenorNota(nota_1)))
print("%i alunos ficaram com %i na prova 2" %(nota_2.count(getMenorNota(nota_2)) ,getMenorNota(nota_2)))
print("%i alunos ficaram com %i na prova 3" %(nota_3.count(getMenorNota(nota_3)) ,getMenorNota(nota_3)))
"""
## Ex5
"""
import random as r

matriz = []
seed = 100
r.seed(seed)

for i in range(12):
    linha = []
    for j in range(12):
        linha.append(r.randint(0, 100))
    matriz.append(linha)

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if(matriz[i][j] => 100):
            print("%2d "% matriz[i][j], end="")
        else: print(" %2d "% matriz[i][j], end="")
    print()

soma_aux = 0
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if (i > j):
            soma_aux += matriz[i][j]
print("Soma: %i"%soma_aux)
"""

    
