import matplotlib.pyplot as plt

from matplotlib import style
import pandas as pd
import pandas_datareader.data as web


style.use('ggplot')

df=pd.read_csv('Alcohol Available for consumption.csv',index_col = 0)
df.plot()
plt.ylabel('Litres (in millions)')
plt.xlabel('Year')
plt.title('Alcohol Available for consumption')
plt.legend.loc = 'top'
plt.show()