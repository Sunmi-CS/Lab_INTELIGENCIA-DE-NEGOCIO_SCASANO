import pandas as pd
print("=" * 60)
print("Ejercicio 1: ventas.csv")
print("=" * 60)

# a) importar archivo y mostrar primeras 5 filas
df_ventas=pd.read_csv("ventas.csv")
print("\na) Primeras 5 filas:")
print(df_ventas.head())

# b) Mostrar el dataset, incluye columnas y tipos de datos
print("\nb) Información general del dataset:")
df_ventas.info()

# c) Cantidad de valores nulos por columna
print("\nc) Valores nulos por columna")
print(df_ventas.isnull().sum())

