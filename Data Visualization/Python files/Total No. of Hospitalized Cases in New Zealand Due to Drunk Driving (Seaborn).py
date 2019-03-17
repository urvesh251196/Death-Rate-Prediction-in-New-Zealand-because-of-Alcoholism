# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df=pd.read_csv('Hospitalize.csv',index_col = 0)


g=sns.pairplot(df, x_vars=['Motorcyclists','Drivers','Cyclist','Other/unknown'], y_vars='YEAR', size=7, aspect=0.7, kind='reg')
i=sns.pairplot(df, x_vars=['Passengers','Pedestrians','Other/unknown'], y_vars='YEAR', size=7, aspect=0.7, kind='reg')


sns.set_context("notebook", font_scale=1.5, rc={"lines.linewidth": 2.5})
sns.set_style("darkgrid")
g.fig.suptitle('Total no. of Hospitalized cases each year due to drunk driving',fontsize=20)
i.fig.suptitle('Total no. of Innocents Hospitalized each year due to drunk driving',fontsize=20)
plt.show()