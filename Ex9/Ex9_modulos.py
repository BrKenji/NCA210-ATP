## Ex1
def alphabeticalOrder(string):
    wordList = string.split("-")
    wordList.sort()
    frase = "-".join(wordList)

    return frase

def countUpperLowerLetters(string):
    upperLetters = 0
    lowerLetters = 0
    for word in string.split("-"):
        for letter in word:
            if(65 <= ord(letter) <= 90):
                upperLetters += 1
            elif(97 <= ord(letter) <= 122):
                lowerLetters += 1
    print("Maiusculas= %i" %upperLetters)
    print("Minusculas= %i" %lowerLetters)

## Ex2
import pandas as pd

def removeClasses(dataFrame):
    newDataFrame = dataFrame.loc[dataFrame['class'].str.contains('ball')]
    newDataFrame = newDataFrame.reset_index()
    
    return newDataFrame

def removeColumns(dataFrame):
    dataFrame = dataFrame.drop(columns = ['height'])
    dataFrame = dataFrame.drop(columns = ['width'])
    dataFrame = dataFrame.drop(columns = ['index'])

    return dataFrame

def editFile(file):
    dataFrame = pd.read_csv(file)
    newDataFrame = removeClasses(dataFrame)
    newDataFrame = removeColumns(newDataFrame)

    newDataFrame.to_csv("new_annotations.csv", index = False)