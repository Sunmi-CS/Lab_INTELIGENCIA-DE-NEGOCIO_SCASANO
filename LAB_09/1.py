import pandas as pd

df = pd.read_csv("01_banco_fuga_clientes.csv")
print("Primeras filas de la base de datos:")
print(df.head())
print("\nInformación de la base de datos:")
print(df.info())
print("\nCantidad de valores nulos por columna:")
print(df.isnull().sum())

X = df.drop("fugo", axis=1)
y = df["fugo"]
print("\nVariables independientes (X):")
print(X.head())
print("\nVariable objetivo (y):")
print(y.head())
