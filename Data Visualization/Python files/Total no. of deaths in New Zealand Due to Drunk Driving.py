import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

style.use('ggplot')


y=[1081,81,826,4059,363]
x=('Bottle Stores','Brewer','Hotels','Restaurants','WineMakers')

x_pos = [x for x in range(len(x))]

plt.bar(x_pos,y, color = 'c' )
plt.xticks(x_pos,y)
plt.title('No. of places where alcoholic drinks can be found')
plt.xlabel('Years')
plt.ylabel('Number of Deaths on roads')
plt.legend()
plt.show()