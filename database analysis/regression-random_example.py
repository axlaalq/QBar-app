import pandas as pd
import numpy as np
import random

# Definir los vectores
General = [21, 10, 12, 9, 8, 6, 9, 7, 10, 11, 10, 15, 13, 20, 12, 19, 18, 19, 25, 20, 17, 12,
           29, 12, 20, 29, 32, 28, 31, 39, 39, 27, 42, 35, 32, 19, 36, 45, 36, 60, 39, 20, 18, 52, 61]

# Generar números aleatorios con media 12, desviación estándar 0.8, entre 3 y 25, redondeados a enteros
np.random.seed(42)
RandomData = np.clip(np.random.normal(loc=12, scale=0.8, size=len(General)), 3, 25).astype(int)
QBar = [RandomData[i]+int(i/5*random.random()) for i in range(0,len(RandomData))]
Event_list=[]
ids=[]
type=[]
for i in range(0,len(General)):
    Event_list.append(General[i])
    Event_list.append(QBar[i])
    ids.append(i)
    ids.append(i)
    type.append('General')
    type.append('QBar')
# Crear el DataFrame
df = pd.DataFrame({'id':ids,'General': Event_list,'Tipo de evento':type})
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme()
sns.set_style("whitegrid")
sns.set(font_scale=1.5)

ax=sns.lmplot(x="id", y="General", data=df,hue = 'Tipo de evento')


plt.rcParams.update({
    "figure.facecolor":  (1.0, 0.0, 0.0, 0.0),  # red   with alpha = 30%
    "axes.facecolor":    (0.0, 1.0, 0.0, 0.0),  # green with alpha = 50%
    "savefig.facecolor": (0.0, 0.0, 1.0, 0.0),  # blue  with alpha = 20%
})
plt.xlabel('Semana')
plt.ylabel('Numero de eventos')
plt.show()
