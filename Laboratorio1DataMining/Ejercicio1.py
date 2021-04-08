# María Isabel Ortiz Naranjo
# Ejercicio Data Mining
# Carné: 18176

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('./fortune500.csv')
df.head()
print(df.info())
df.columns = ['year', 'rank_', 'company', 'revenue', 'profit']
print(df.info())
df.head()
print(df.info())
print("La cantidad de registros: 25500")
df.dtypes
print(df.info())

# Investigue con la herramienta que está utilizando cómo puede desplegar los casos que no se están 
# logrando convertir a enteros para poder tener una idea de contra quénos estamos enfrentando.

numb = df.loc[df.profit.str.contains('[^0-9.-]')]
numb.head()
print(numb.info())
print("cantidad de registros: {}".format(len(numb)))

# Gráfica

graphic_plot = numb.year.plot.hist(bins=numb.year.max()-numb.year.min())
graphic_plot.set_ylabel("")

df.drop(df.index[df['profit'] == 'N.A.'], inplace = True)
# Muestra de la gráfica 
plt.show()

print("registros eliminados {}".format(len(df)))

df = df.astype({"profit": float})
df.dtypes
print(df.info())

# Gráfica de ganancia promedio

profit_average = df.groupby(["year"]).mean()
profitplot = profit_average["profit"].plot(title=" Ganancia promedio de 1955 al 2005", color='#6283B4')
profitplot.grid(color="white")
profitplot.set_facecolor('#EAEAF5')
profitplot.set_ylabel("Ganancias")
profitplot.set_xlabel("")

# Muestra de la gráfica 
plt.show()

# Grafica de promedio de ingresos

profitplot2 = profit_average["revenue"].plot(title="Promedio de ingresos del 1955 al 2005", color='#6283B4')
profitplot2.grid(color="white")
profitplot2.set_facecolor('#EAEAF5')
profitplot2.set_ylabel("Ingresos (En millones)")
profitplot2.set_xlabel("")

# Muestra de la gráfica 
plt.show()
