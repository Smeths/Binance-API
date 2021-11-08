# importing libraries
from time import time, ctime
import json
import requests
import pandas as pd

# setting parameters for call
symbol = "BTCUSDT"
params=dict(symbol=symbol,limit=1)

# total trade interval
strTime = time()
tmDisPrevTime = time()
totTrdPeriod = 90000 # time is secs
tmDisTS = 30 # time step in secs. (Time discretisation, one mu 
tmDisnTS = 0
c = ","

# return data file
f = open(symbol +"_PriceTime.csv", "w")
f.write("Actual Time, Return Status, Trade Time, Price \n")

# implement total trading interval   
while time() - strTime < totTrdPeriod:
# implement time discretisation
    if time() - tmDisPrevTime > tmDisTS:
# updating time data
        tmDisnTS = tmDisnTS + 1    
        tmDisPrevTime = time()
# calling api
        r = requests.get('https://api.binance.com/api/v3/trades',params=params)
        rdict = r.json()
# writing data to a file
        tradeData = str(time()) + c + str(r.status_code) + c + str(rdict[0]["time"]) + c + str(rdict[0]["price"]) + "\n"
        f.write(tradeData)
        print("Number of Data Points: " + str(tmDisnTS))





