## Ex1
"""
while True:
    letra = str(input("Digite a letra desejada: "))

    if (letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u"):
        print("Essa letra é uma vogal")
    elif(letra == "y"):
        print("Essa letra, em algumas línguas, pode ser considerada como uma vogal e, em outras, como uma consoante.")
    else:
        print("Essa letra é uma consoante.")
"""

## Ex2
"""
while True:
    row = int(input("Digite a linha desejada: "))
    col = str(input("Digite a coluna desejada: "))

    aux_1 = ["a", "c", "e", "g"]
    aux_2 = ["b", "d", "f", "h"]

    if((col in aux_1 and row%2 == 1) or (col in aux_2 and row%2 == 0)):
       print("Preto")
    else:
        print("Branco")
"""

## Ex3
"""
ano_contratado = 2005
salario_inc = 5000.00

ano_aux = 2006

bonus_atual = 0.015
salario_atual = salario_inc*(1+bonus_atual)

ano_atual = int(input("Digite o ano desejado: "))

if(ano_atual == 2006):
    print("Salário de %i: R$ %.2f " %(ano_atual, salario_atual))
elif(ano_atual > 2006):
    while(ano_aux < ano_atual):
        bonus_atual *= 2
        salario_atual *= (1+ bonus_atual)
        ano_aux += 1
    print("Salário de %i: R$ %.2f " %(ano_atual, salario_atual))
"""

## Ex4
"""
while True:
    d = 0

    n = int(input("Digite n: "))
    m = int(input("Digite m: "))

    if(n > m):
        d += n
    else:
        d += m

    while(d > 0):
        if((m%d == 0) and (n%d ==0)):
            break
        d -= 1

    print(d)
"""

## Ex5
"""
x = int(input("Digite o número desejado: "))

p = x/2
erro = abs(p**2 - x)

while(erro > 10**-12):
    p = (p + x/p)/2
    erro = p**2 - x
print("%.3f" %p)
"""

## Ex6
"""
while True:
    day = int(input("Digite o dia desejado: "))
    month = str(input("Digite o mês desejado: "))

    if(month == "janeiro" or month == "fevereiro"):
        print("Verão")
    elif(month == "março" and 1 <= day < 20):
        print("Verão")
    elif(month == "março" and 20 <= day <= 31):
        print("Outono")
    elif(month == "abril" or month == "maio"):
        print("Outono")
    elif(month == "junho" and 1 <= day < 21):
        print("Outono")
    elif(month == "junho" and 21 <= day <=30):
        print("Inverno")
    elif(month == "julho" or month == "agosto"):
        print("Inverno")
    elif(month == "setembro" and 1 <= day < 22):
        print("Inverno")
    elif(month == "setembro" and 22 <= day < 30):
        print("Primavera")
    elif(month == "outubro" or month == "novembro"):
        print("Primavera")
    elif(month == "dezembro" and 1 <= day < 21):
        print("Primavera")
    elif(month == "dezembro" and 21 <= day < 31):
        print("Verão")
"""


    




    

