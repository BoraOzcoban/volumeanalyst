import pandas_datareader.data as web

x = input("Name of the stock/ currency: ")
start = input("Enter the graph's start date(M/D/Y): ")
end = input("Enter the graph's end date(M/D/Y): ")

stock = web.DataReader(x, "yahoo", start, end)
stock.sort_values(by=['Volume'], inplace=True, ascending=False)

o = stock["Open"]
c = stock["Close"]
x = (100 * c) / o
y = x - 100
stock["Percentage"] = y

print(stock[["Open", "Close", "Volume", "Percentage"]].head(10))
