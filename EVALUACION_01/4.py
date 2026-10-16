import pandas as pd
empleados = pd.read_csv("P04_empleados.csv")

print("primeras 5 filas:")
print(empleados.head())

print("\nvalores nulos por columna:")
print(empleados.isnull().sum())