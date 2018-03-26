import pandas as pd
import quandl
import numpy as np
import matplotlib.pyplot as plt
import movingaverage as ma

tdf = ma.SMA('AMZN', '2016-01-01', '2017-12-31', 20)
odf = ma.SMA('AMZN', '2016-01-01', '2017-12-31', 100)

plt.figure()
x = tdf['Date']
y1 = tdf['Adj. Close']
y2 = tdf['20-days SMA']
y3 = odf['100-days SMA']

plt.plot(x,y1, label="Price")
plt.plot(x,y2, label="20-Days SMA")
plt.plot(x,y3, label="100-Days SMA")
plt.legend(loc='upper left')
plt.xlabel('Date')
plt.ylabel('Price in $')
plt.suptitle('AMZN')
plt.show()
