import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import pyplot, pylab
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

import numpy as np

style.use('ggplot')


y=pd.read_csv('Innocents.csv', index_col=0)
y.plot()

plt.xlabel('Years')
plt.ylabel('Counts')
plt.title('Number of Innocents Killed due to Drunk Driving')
plt.legend.loc = 'best'
plt.show()