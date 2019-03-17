import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import pyplot, pylab
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import numpy as np
import matplotlib.ticker as ticker

style.use('ggplot')

df=pd.read_csv('crashes.csv')
df1=pd.read_csv('crashes.csv')

x=[1999,2001,2003,2005,2007,2009,2011,2013,2015]

plt.plot(df['Quarter'],df['Crashes'])
plt.plot(df1['Quarter'],df1['Deaths'])
plt.rcParams['axes.facecolor'] = 'white'

plt.xlim(1999,2016)
plt.xticks(x,x)
plt.title('Total no. of Crashes and Deaths in New Zealand due to Drunk Driving')
plt.xlabel('Years')
plt.ylabel('Total Incidents')
plt.legend()
plt.show()