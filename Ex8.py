## Ex1
"""
codigo_morse = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....',
 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.',
  'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '0':'-----', '1':'.----',
   '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.'}

def converte(dict, string):
    string = string.replace("!", "").replace(",", "")

    letras = [x for x in string if (x != " ")]
    
    morseConv = ""
    for letter in letras:
        key = letter.upper()
        morseConv += str(dict.get(key)) + " "

    return morseConv

print(converte(codigo_morse, "Hello World!!!"))
"""
## Ex2
"""
frase = "Um teste, dois testes, mais testes, acabou?, SIM !!!"

def contaPalavras(frase):
    frase = frase.replace(",", "").replace("?", "").replace("!", "").split()
    wordsList = [x.lower() for x in frase]
    aux = []
    dict = {}

    for i in wordsList: 
        if(aux.count(i) == 0): aux.append(i)
    for i in aux:
        dict[i] = wordsList.count(i)

    return dict
    
print(contaPalavras(frase))
"""
## Ex3

itemsData = {'maça': {'Quantidade': 100, 'Preco': 1.5} , 'banana': {'Quantidade': 12, 'Preco': 3.2} }
operations = ["1", "2", "3", "4", "5"]

def main():
    global itemsData
    while (True):
        menu()
        switch(receiveOption())
        print("")

def menu():
    print("*"*55)
    print("Operação 1: Inserir um item")
    print("Operação 2: Remover um item")
    print("Operação 3: Atualizar o preço de algum item")
    print("Operação 4: Atualizar estoque")
    print("Operação 5: Imprimir dados do estoque")
    print("*"*55)

def receiveOption():
    option = str(input("Escolha o número da operação desejada: "))
    while (option not in operations):
        print("Número inserido inválido !!!")
        option = str(input("Escolha o número da operação desejada: "))
    return option

def switch(case):
    if (case == "1"): return addItem()
    elif (case == "2"): return removeItem()
    elif (case == "3"): return updatePrice()
    elif (case == "4"): return updateStock()
    else: print(itemsData)

def addItem():
    global itemsData
    print("")
    itemName = str(input("Nome do produto que deseja adicionar: ")).lower()
    if (itemName in itemsData):
        print("Esse item já existe !")
    else:
        itemPrice = float(input("Preço do produto: "))
        itemAmount = int(input("Quantidade do produto: "))
        itemsData[itemName] = {}
        itemsData[itemName]["Quantidade"] = itemAmount
        itemsData[itemName]["Preco"] = itemPrice
        print("O item %s foi adicionado" %itemName)

def removeItem():
    global itemsData
    print("")
    itemName = str(input("Nome do item que deseja remover: ")).lower()
    if (itemName not in itemsData):
        print("Esse item não existe no estoque !")
    else:
        itemsData.pop(itemName)
        print("O item %s foi removido" %itemName)

def updatePrice():
    global itemsData
    print("")
    itemName = str(input("Nome do produto: ")).lower()

    if (itemName.lower() not in itemsData):
        print("Esse item não existe no estoque !")
    else:
        newPrice = float(input("Novo preço: "))
        itemsData[itemName]["Preco"] = newPrice
        print("Preço do item %s foi atualizado" %itemName)

def updateStock():
    global itemsData
    print("")
    itemName = str(input("Nome do produto: ")).lower()
    if (itemName not in itemsData):
        print("Esse item não existe no estoque !")
    else:
        newAmount = int(input("Nova quantia do produto: "))
        itemsData[itemName]["Quantidade"] = newAmount
        print("A quantidade do produto %s foi atualizada" %itemName)

main()