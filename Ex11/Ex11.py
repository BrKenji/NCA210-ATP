import matplotlib.pyplot as plt
from numpy import split
import pandas as pd

## Ex1
"""
df = pd.read_csv("./gold_prices_monthly.csv")
fig, axis = plt.subplots()

axis.plot( df["Date"], df["Price"], label = "Preço do Ouro")
plt.style.use('classic')
plt.title("Preço Histórico do Ouro")
plt.xlabel("Datas")
plt.ylabel("Preço (R$)")
leg = axis.legend()
axis.legend(loc='upper left', ncol=2,shadow=True, borderpad=1, frameon=False)
plt.show()
"""
## Ex2
"""
df = pd.read_csv("./SP500_prices_monthly.csv")
df_list = []
year_list = []
mean_prices_list = []

year_start = 2000
year_end = 2010

# Fills year_list with the years used on the plot
for i in range(year_start, year_end + 1) :
    year_list.append(str(i))
# Fills df_list with the dataframes of each year
for year in year_list:
    df_list.append(df[df["Date"].str.contains(year)])
# Fills mean_prices_list with the mean prices of each dataframe
for dataframe in df_list:
    mean_prices_list.append(dataframe["Price"].mean())

fig, axis = plt.subplots()
plt.bar(year_list, mean_prices_list)
plt.title("Média Anual do Preço Histórico da Bolsa de NY")
plt.ylabel("Preço (USD)")
plt.xlabel("Ano")
plt.show()
"""
## Ex3
"""
# linha de raciocínio: o arquivo gold_price_monthly.csv já mostar o preço mensal do ouro,
# então para satisfazer a parte da comparação referente ao prço mensal do mês do ouro apenas
# filtrei o arquivo e armazenei num dataframe novo com os preços mensais dentro do período
# e para plotar usei apenas as colunas do dataframe, para satisfazer a segunda parte, preço do
# último dia do mês do histórico da bolsa de NY, como o arquivo SP500_prices_monthly.csv faz
# a atualização do preço todo dia 01 do mês, então, por exemplo, foi considerado o preço
# do dia 1997-10-01 com sendo o preço do dia 1997-09-31, ou seja, úlitmo dia do mês anterior.

gold_price_df = pd.read_csv("./gold_prices_monthly.csv")
stock_price_df = pd.read_csv("./SP500_prices_monthly.csv")

year_start = 2000
year_end = 2015

gold_price_list = []
stock_price_list = []

for year in range(year_start, year_end + 1):
    gold_price_list.append(gold_price_df[gold_price_df["Date"].str.startswith(str(year))])
    stock_price_list.append(stock_price_df[stock_price_df["Date"].str.contains(str(year))])

new_gold_price_df = pd.concat(gold_price_list).reset_index()
new_stock_price_df = pd.concat(stock_price_list).reset_index()

# Deletes the column labeled "index"
del new_stock_price_df["index"]

index = new_stock_price_df.index

dummy_stock_df = new_stock_price_df

for year in dummy_stock_df["Date"]:
    # o arquivo SP500_prices_monthly.csv salva a data num formato diferente do arquivo
    # gold_prices_monthly.csv, então nesse bloco, cortamos o dia do mês para que no plot
    # ambos gráficos tenham o mesmo valores/formato, ano-mês.
    condition = dummy_stock_df["Date"] == year
    year_index = index[condition]
    new_stock_price_df.at[year_index, "Date"] = year[0:7:1]

fig, axis = plt.subplots()
xmin, xmax = plt.xlim()

plt.title("Comparação do Preço Mensal do Ouro e o Preço da Bolsa de NY")
axis.plot(new_gold_price_df["Date"], new_gold_price_df["Price"], label = "Preço do Mensal Ouro")
axis.plot(new_stock_price_df["Date"], new_stock_price_df["Price"], label = "Preço da Ação no Último Dia do Mês")
plt.xlabel("Data")
plt.ylabel("Preço (USD)")
plt.legend()
plt.show()
"""