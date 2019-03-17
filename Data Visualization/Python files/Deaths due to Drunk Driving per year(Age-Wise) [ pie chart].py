import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import numpy as np

style.use('ggplot')

x=['886','1713','766']

y= ['15-24','25-59','60+']
cols= ['r','b','g']
plt.pie(x, labels=y,colors=cols,autopct='%1.1f%%')
plt.title('Total no. of Deaths Due to Drunk Driving(Age-Wise)')

plt.show()