import pandas_datareader.data as web
import matplotlib.pyplot as plt

x = input("Name of the stock:")
y = int(input("MA One:"))
z = int(input("MA Two:"))

start = input("Enter the graph's start date(M/D/Y)")
end = input("Enter the graph's end date(M/D/Y)")

stock = web.DataReader(x, "yahoo", start, end)
stock[f"MA{y}"] = stock["Open"].rolling(y).mean()
stock[f"MA{z}"] = stock["Open"].rolling(z).mean()
stock["Open"].plot(figsize=(16, 8))
stock[f"MA{y}"].plot()
stock[f"MA{z}"].plot()

plt.legend()
plt.show()

