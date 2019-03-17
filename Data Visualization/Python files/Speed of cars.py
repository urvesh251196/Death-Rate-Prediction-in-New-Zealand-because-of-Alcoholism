import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd

style.use('ggplot')

y=pd.read_csv('Speedlimit.csv',index_col=0)
y.plot()

plt.title('Speed Of Drivers')
plt.legend.loc = 'best'
plt.show()