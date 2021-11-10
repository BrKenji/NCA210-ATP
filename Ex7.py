## Ex1
"""
import os

def verifica(file):
    return os.path.isfile(file)

	
print(verifica('./Texts/Lusiadas.txt'))
print(verifica('./Texts/aula.txt'))
"""
## Ex2
"""
def file_info(file):
    linhas = 0
    palavras = 0
    caracteres = 0
    arquivo = open(file, encoding="utf-8")
    for line in arquivo:
        linhas +=1
        palavras += len(line.split())
        for word in line:
            caracteres += len(word)

    arquivo.close()

    return linhas, palavras, caracteres

print(file_info("./Texts/Lusiadas.txt"))
"""
## Ex3
"""
def somatorio(file):
    arquivo = open(file, "r")
    numeros = [int(x) for x in arquivo.readline().split()]
    return sum(numeros)

print(somatorio("./Texts/numeros.txt"))
"""
## Ex4
"""
def spellChecker(string):
    list = [x.lower() for x in string.replace(",", "").split()]

    with open("words.txt", "r") as arquivo:
        arquivo.seek(0)
        lines = arquivo.read().lower().splitlines()     
        list2 = [word for word in list if(word not in lines)]
    
    return list2
 
print(spellChecker("Hello World, Olá Mundo"))
"""
## Ex5

fileName = str(input("Nome do arquivo: "))
novoNome = str(input("Novo nome: "))

def removeComments(arquivo, string):
    newFile = open(string, "w")
    with open(fileName, "r") as file:
        file.seek(0)
        lines = file.read().splitlines()
        for i in lines:
            if ("#" in i):
                splitString = i.split("#", 1)
                newFile.write(splitString[0])
                newFile.write("\n")
            else:
                newFile.write(i)
                newFile.write("\n")

    file.close()
    newFile.close()

removeComments(fileName, novoNome)



