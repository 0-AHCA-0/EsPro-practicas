import pandas as pd

ventas = pd.read_csv("data/ventas.csv")
ventas["ticket"] = ventas["ventas"]/ventas["clientes"] ##nueva columna
print(ventas.head())

##imprimir el maximo en ventas
print("\n")
#print(ventas["ventas"].max())

##localizar indice o tupla asociado a un identificador, en este caso, la 
##sucursal con mayor ventas 
print("Sucursal con mayor ventas", 
      ventas.loc[ventas["ventas"].idxmax(), "sucursal"])

##imprimir la sucursal con menor ventas
print("Sucursal con menor ventas",
      ventas.loc[ventas["ventas"].idxmin(), "sucursal"])