# importing libraries
from time import time, ctime
import json
import requests
import pandas as pd

# setting parameters for call
params=dict(symbol="BTCUSDT",limit=1000)
# calling api
r = requests.get('https://api.binance.com/api/v3/trades',params=params)
print("Check return status. 200 means returned ok")
print(r.status_code)
rdict = r.json()

# printing trades returned
print("trades data returned")
print(rdict[0])
print(rdict[999])
# turn time returned into something "human readable"
print("just the time of the trade")
print(ctime(float(rdict[0]['time'])/(10**3)))
print(ctime(float(rdict[999]['time'])/(10**3)))





