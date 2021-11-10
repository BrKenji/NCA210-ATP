import pandas as pd
from pandas.core import indexing

## Ex1
"""
df = pd.read_csv("./annotations.csv")
# drop width and height columns
df.drop(['width', 'height'], axis='columns', inplace=True)

# Get indexes where class isn't 'ball'
notBallIndexes = df[df['class'] != 'ball'].index
 
# Delete these row indexes from dataFrame
df.drop(notBallIndexes , inplace=True)
# print(df.to_string())
"""
## Ex2
"""
atividadesDf = pd.read_excel('notasAtividades.xlsx').set_index("Nome")
projetoDf = pd.read_excel('notasProjetosProvas.xlsx').set_index("Nome")

# Cria um dataframe vazio apenas com os nomes das colunas
newFile = pd.DataFrame(columns = ["Média Atividades","Projeto", "Prova", "Média Final"])
# Média das atividades
newFile["Média Atividades"] = atividadesDf[list(atividadesDf)].sum(axis=1)/atividadesDf.count(axis="columns")
# Nota da prova
newFile["Prova"] = projetoDf["Prova"]
# Média ponderada do projeto
newFile["Projeto"] = projetoDf["Projeto Parcial"]*0.2 + projetoDf["Projeto Final"]*0.8
# Média Final
newFile["Média Final"] = round((newFile["Média Atividades"] + 2*newFile["Projeto"] + 3*newFile["Prova"])/6, 2)
# Save new dateframe to excel file
newFile.to_excel("resultadosFinais.xlsx")
print(newFile.to_string())
"""
## Ex3
"""
schooList = []

data = {
    'school': ['s001', 's002', 's003', 's001', 's002', 's003'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_of_birth': ['15/05/2002', '17/05/2002', '16/02/1999', '25/09/1998', '11/05/2002', '15/09/1997'],
    'age': [12, 12, 13, 13, 14, 12],
    'height' : [173, 192, 186, 167, 151, 159],
    'weight' : [35, 32, 33, 30, 31, 32] 
}

df = pd.DataFrame(data, index=['S1', 'S2', 'S3', 'S4', 'S5', 'S6'])

# Filtering dataframe and assingning it to new variables then adding each to schooList
minAgeS001 = df.loc[(df["school"] == "s001")]
schooList.append(minAgeS001)
minAgeS002 = df.loc[(df["school"] == "s002")]
schooList.append(minAgeS002)
minAgeS003 = df.loc[(df["school"] == "s003")]
schooList.append(minAgeS003)

for dataframe in schooList:
    print("\nEscola %s" %dataframe.iloc[0]["school"])
    print("Menor idade: %i" %dataframe["age"].min())
    print("Maior idade: %i" %dataframe["age"].max())
    print("Média de idade: %.1f" %dataframe["age"].mean())
"""