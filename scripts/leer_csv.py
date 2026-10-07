import pandas as pd

ventas = pd.read_csv('data/ventas.csv')

#Imprimir una vista previa de las primeras filas del DataFrame y sus dimensiones
print("Vista previa de las primeras filas del DataFrame:")
print(ventas.head)
#Imprimir las dimensiones del DataFrame
print("Dimensiones del DataFrame:")
print(ventas.shape)
#Imprimir los tipos de datos de cada columna del DataFrame
print("Tipos de datos de cada columna:")
print(ventas.dtypes)