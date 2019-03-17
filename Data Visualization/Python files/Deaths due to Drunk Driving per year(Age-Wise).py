import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import numpy as np


style.use('ggplot')

df=pd.read_csv('Drivers age.csv', index_col=0)
#df.xlabel('Time Period')
#df.ylabel('No. of Deaths')
#df.title('Deaths due to Drunk Driving per year\n(Age-Wise)')
df.plot()
plt.show()