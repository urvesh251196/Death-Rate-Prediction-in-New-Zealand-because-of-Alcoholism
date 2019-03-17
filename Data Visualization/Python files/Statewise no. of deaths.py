import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import pyplot, pylab
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import xlrd
import numpy as np

style.use('ggplot')

x=['Northland','Auckland','Waikato','Bay of Plenty','Gisborne','HawkesBay','Taranaki','Manawatu/Wanganui','Wellington','Nelson/Marlborough','West Coast','Canterbury','Otago','Southland']
y=[144,345,324,174,52,92,55,138,92,53,26,187,65,61]

cols= ['m','mediumslateblue','c','y','g','r','pink','maroon','indigo','lightcoral','firebrick','lavender','aquamarine','thistle']
plt.pie(y, labels = x , colors = cols,explode=(0,0.1,0,0,0,0,0,0,0,0,0,0,0,0), autopct='%1.1f%%')
plt.title('Total no. of deaths Statewise')
plt.legend.loc = 'best'
plt.show()