# Maria Isabel Ortiz Naranjo
# Carné 18176
# Laboratorio 2

from copy import deepcopy
import numpy as np
import pandas as pd 
from matplotlib import pyplot as plt

flor = pd.read_csv("iris.csv") 
flor.head()
print(flor.info)

# Sepalo
fig = flor[flor.flower == 'flor-setosa'].plot(kind='scatter',  x='sepal_length', y='sepal_width', color='blue', label='Setosa')
flor[flor.flower == 'flor-versicolor'].plot(kind='scatter', x='sepal_length', y='sepal_width', color='green', label='Versicolor', ax=fig)
flor[flor.flower == 'flor-virginica'].plot(kind='scatter', x='sepal_length', y='sepal_width', color='red', label='Virginica', ax=fig)
# Longitud 
fig.set_xlabel('Longitud')
# Ancho
fig.set_ylabel('Ancho')
fig.set_title('Sepalo')
plt.show()

# Pétalo
fig = flor[flor.flower == 'flor-setosa'].plot(kind='scatter', x='petal_length', y='petal_width', color='blue', label='Setosa')
flor[flor.flower == 'flor-versicolor'].plot(kind='scatter', x='petal_length', y='petal_width', color='green', label='Versicolor', ax=fig)
flor[flor.flower == 'flor-virginica'].plot(kind='scatter', x='petal_length', y='petal_width', color='red', label='Virginica', ax=fig)
# Longitud 
fig.set_xlabel('Longitud')
# Ancho 
fig.set_ylabel('Ancho')
fig.set_title('Pétalo')
plt.show()