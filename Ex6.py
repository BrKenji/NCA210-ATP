## Ex1
"""
def contaPalavras(frase):
    lista = frase.split()
    return len(lista)
"""
## Ex2
"""
def maiorPalavra(frase):
    frase = frase.replace(",", "")
    lista = frase.split()
    maior = lista[0]

    for i in lista:
        if(len(i) > len(maior)):
            maior = i


    lista_aux = [x for x in lista if(len(x) == len(maior))]

    for i in lista_aux:
        while(lista_aux.count(i) > 1): lista_aux.remove(i)

    return len(maior), lista_aux

print(maiorPalavra("A Maria ama laranja, abacaxi e uva, mas não gosta de suco de abacaxi"))
"""
## Ex3
"""
def contaPalavras(frase):
    frase = frase.replace(",", "")
    frase = frase.replace("!", "")
    frase = frase.replace("?", "")

    list = [x.lower() for x in frase.split()]
    
    list_aux  = []

    for i in list:    
        if(list_aux.count(i) == 0 and len(i) > 1): list_aux.append(i)
    
    list_count = [list.count(x) for x in list_aux]

    return list_aux, list_count

s = "Testando com teste para testar o que com teste se testa, se o teste está testando com teste, passou no teste?"
print(contaPalavras(s))
"""
## Ex4
"""
def nomeCitacao(nome):
    nome = nome.split()
    print("%s, %s" %(nome[-1], nome[0]))

nomeCitacao("Paulo Santos")
"""

## Ex5
"""
TAM_MAX_CH = 26

def criptCesar(mensagem, chave):
    traduzido = ''

    for simbolo in mensagem:
        if simbolo.isalpha():
            num = ord(simbolo)
            num += chave

            if simbolo.isupper():
                if num > ord('Z'):
                    num -= TAM_MAX_CH
                elif num < ord('A'):
                    num += TAM_MAX_CH
            elif simbolo.islower():
                if num > ord('z'):
                    num -= TAM_MAX_CH
                elif num < ord('a'):
                    num += TAM_MAX_CH
            traduzido += chr(num)
        else:
            traduzido += simbolo
    return traduzido

p = "ISAAC !@ZABC"
print(criptCesar(p, 1))
"""