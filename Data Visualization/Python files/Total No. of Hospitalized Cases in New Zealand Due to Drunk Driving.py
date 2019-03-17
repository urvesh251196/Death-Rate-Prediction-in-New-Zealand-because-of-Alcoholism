
import matplotlib.pyplot as plt

from matplotlib import style
import pandas as pd
import pandas_datareader.data as web


style.use('ggplot')

df=pd.read_csv('Hospitalize.csv',index_col = 0)
df.plot()
plt.ylabel('Number of People hospitalized')
plt.xlabel('Year')
plt.title('Total No. of Hospitalized Cases in New Zealand Due to Drunk Driving')
plt.legend.loc = 'best'
plt.show()