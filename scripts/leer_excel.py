# Formato de archivo: UTF-8
# leer_excel.py — Cargar el reporte Excel de la API (Python)

import pandas as pd 
ventas = pd.read_excel('data/ventas.xlsx')

print("Primera vista del excel nya:")
print(ventas.head())
print("Dimensiones del DataFrame:")
print(ventas.shape)
print("Tipos de datos de cada columna:")
print(ventas.dtypes)



