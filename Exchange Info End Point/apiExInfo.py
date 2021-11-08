# importing libraries
import json
import requests
import pandas as pd

# downloading data into a dictionary
r = requests.get('https://api.binance.com/api/v3/exchangeInfo')
rdict = r.json()

# looping over rate limits
data = []
for i,rate in enumerate(rdict["rateLimits"]):
    data.append([rate["rateLimitType"],rate["interval"],rate["intervalNum"],rate["limit"]])

# outputing data to csv
columns = ["rateLimitType","interval","intervalNum","limit"]
df = pd.DataFrame(data=data,columns=columns)
df.to_csv("rates.csv",index=False)

# looping over symbol data
data = []
for i,symbol in enumerate(rdict["symbols"]):
    data.append([symbol["symbol"],symbol["status"]])

# outputing data to csv
columns = ["symbol","status"]
df = pd.DataFrame(data=data,columns=columns)
df.to_csv("symbols.csv",index=False)



