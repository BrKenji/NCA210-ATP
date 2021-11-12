import matplotlib.pyplot as plt
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
plt.title("Média Anual do Preço Histórioco da Bolsa de NY")
plt.ylabel("Preço (USD)")
plt.xlabel("Ano")
plt.show()
"""
