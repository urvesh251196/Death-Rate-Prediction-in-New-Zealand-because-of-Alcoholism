
import matplotlib.pyplot as plt

from matplotlib import style
import pandas as pd
import pandas_datareader.data as web


style.use('ggplot')

df=pd.read_csv('pure alcohol available for consumption.csv',index_col = 0)
df.plot(linewidth=2)
plt.ylabel('Litres (in millions)')
plt.xlabel('Year')
plt.title('Volume of pure alcohol available')
plt.legend.loc = 'best'
plt.show()