stocks = {
    'GOOG': 434,
    'APPL': 325,
    'FB': 54,
    'AMZN': 623,
    'F': 32,
    'MSFT': 549

}

# (434, GOOG) format

min_price = min(zip(stocks.values(), stocks.keys()))
print(min_price)