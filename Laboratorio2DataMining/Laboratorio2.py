# Maria Isabel Ortiz Naranjo
# Carné 18176
# Laboratorio 2

from copy import deepcopy
import numpy as np
import pandas as pd 
from matplotlib import pyplot as plt

flor = pd.read_csv('./iris.csv') 
flor.head()
print(flor.head())

fig = flor[flor.flower == 'Iris-setosa'].plot(kind='scatter',  x='sepal_length', y='sepal_width', color='blue', label='Setosa')
flor[flor.flower == 'Iris-versicolor'].plot(kind='scatter', x='sepal_length', y='sepal_width', color='green', label='Versicolor', ax=fig)
flor[flor.flower == 'Iris-virginica'].plot(kind='scatter', x='sepal_length', y='sepal_width', color='red', label='Virginica', ax=fig)
fig.set_xlabel('Sépalo - Longitud')
fig.set_ylabel('Sépalo - Ancho')
fig.set_title('Sépalo - Longitud vs Ancho')
plt.show()