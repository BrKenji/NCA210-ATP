# Qual será a saída do seguinte código em Python?
"""
x = 5
def f1():
    global x
    x = 4

def f2(a, b):
    x = 3
    return a + b + x

total = f2(1, 2)
f1()
print(total)
"""
# Dado o programa abaixo, Qual será o valor  retornado pela função compute_bill executando o programa (na função  print) ?
"""
def compute_bill(lista):
    stock = {
        "banana": 2,
        "pera": 4, 
        "uva": 37,
        "melancia": 0
    }

    prices = {
        "banana": 2,
        "pera": 5, 
        "uva": 7.5,
        "melancia": 10
    }

    total = 0
    naoComprado = []
    for x in lista:
        preco = prices[x]
        if (stock[x] > 0):
            total+=preco
            stock[x]-=1
        else:
            naoComprado.append(x)
    return total, naoComprado

lista_de_compras = ["banana", "pera", "melancia"]
print(compute_bill(lista_de_compras))
"""
# Um aluno de Engenharia quer montar um painel matricial de Letras usando LEDs, porém ele não possui muitos LEDs,
# e não tem certeza se conseguirá escrever as palavras desejadas. Considerando a configuração dos leds das Letras da
# Figura abaixo, crie um algoritmo que ajude a descobrir a quantidade de leds necessário para escrever uma palavra.
"""
dict = {
    "A": 20,
    "E": 20,
    "S": 17,
    "O": 20,
    "U": 19,
    "L": 13,
    "P": 18,
    "R": 22,
    "V": 17,
    "T": 13,
}

while(True):
    word = str(input("Digite uma palavra: ")).upper()

    ledsNumber = 0

    for letter in word:
        if (letter in dict):
            ledsNumber += dict[letter]
        else:
            print("Não é possível mostrar essa palavra completa")
            break
    print("N de LEDS: %i" %ledsNumber)
"""
# Dado o programa abaixo, Preencha corretamente a Tabela com os valores da matriz após a execução do programa:
"""
matriz = [[4, 1, 20, 3], [1, 8, 4], [5.1, 3, 8, 0]]
matriz.insert(2, [1.2, 4, 7, 2])
matriz.pop(3)
matriz[1].append(8)
matriz[1][2] = 1.7
matriz[1][1] = 'b'
matriz[0][2] = 12
matriz[0][1] = 9 
print(matriz)
"""
# Analise o programa abaixo e responda a questão:
"""
C = 0
D = 0

for contador in range(2, 5):
    if (C == 4):
        C += 3
    else:
        C += 2

for contador in range(3, 8):
    if (D == 4):
        D += 1
    else:
        D += 2

while(C < 4):
    if(D == 4):
        D += 1
    else:
        D += 2

while(D < 4):
    if(D == 4):
        C += 3
    else:
        C += 2

print("C: %i e D: %i" %(C, D))
"""
# Um programador precisa realizar o cálculo da média dos valores contidos dentro de alguns arquivos, esses arquivos
# possuem os valores de leitura da corrente elétrica, no entanto o aparelho que realiza a leitura está apresentando
# alguns valores como nan quando não consegue realizar a leitura, porém, está salvando esses valores no arquivo.
# Escreva uma função chamada mediaCorrente() que recebe como parâmetro o nome de um arquivo (os arquivos já
# estão previamente adicionados no Moodle para os testes), e realize o calculo da média dos valores contidos nesse
# ivo, retornando um número inteiro desse valor da média.
"""
def mediaCorrente(file):
    sum = sampleQtd = 0

    file = open(file, 'r')
    for line in file:
        if(line.replace("\n", "") == 'nan'):
            pass
        else:
            sum += float(line)
            sampleQtd += 1

    return int(sum/sampleQtd)

print(mediaCorrente("./corrente.txt"))
"""
