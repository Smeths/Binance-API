# importing libraries
from time import time, ctime
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Importing trade data
fname = "BTCUSDT_PriceTime.csv"
tradeData = np.loadtxt(fname,skiprows=1,delimiter=",")
tradeTime = tradeData[:,2]/(10**3)
tradeTime0 = tradeData[0,2]/(10**3)
tradePrice = tradeData[:,3]

# plotting trade data
fig, axs = plt.subplots()
axs.scatter(tradeTime - tradeTime0,tradePrice)
axs.set_title(ctime(tradeTime[0]))
axs.set_xlabel("Seconds Past: "+ctime(tradeTime[0]))
axs.set_ylabel("Price: "+fname[0:6])
plt.savefig("priceVtime.png")







