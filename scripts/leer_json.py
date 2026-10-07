import pandas as pd 
import json 


with open('data/ventas.json') as f:
    data = json.load(f)
ventas = pd.json_normalize(data)    
print("Vista previa de las primeras filas del DataFrame:")
print(ventas.head())
print("Dimensiones del DataFrame:")
print(ventas.shape)
print("Tipos de datos de cada columna:")
print(ventas.dtypes)


# leer_json.py — Cargar el reporte JSON de la API (Python)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
#   python scripts/leer_json.py

# TODO 1: importa json y pandas
# TODO 2: carga data/ventas.json con json.load
# TODO 3: convierte la lista de diccionarios en un DataFrame
#         (recuerda del cap. 2: el JSON no llega como tabla directa)
# TODO 4: imprime las dimensiones y las primeras filas
