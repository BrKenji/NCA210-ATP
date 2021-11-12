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