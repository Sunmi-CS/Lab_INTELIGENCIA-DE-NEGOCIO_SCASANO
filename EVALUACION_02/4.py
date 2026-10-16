
import pandas as pd
import numpy as np

datos = {
    "Estudiante": ["Ana", "Luis", "Carlos", "María", "José", "Lucía", "Pedro"],
    "Nota": [15, 12, np.nan, 18, 14, np.nan, 16]
}

df = pd.DataFrame(datos)

print("DataFrame original:")
print(df)

print("\nValores faltantes por columna:")
print(df.isnull().sum())

media = df["Nota"].mean()
print("\nMedia de las notas:", media)

df["Nota"] = df["Nota"].fillna(media)

print("\nDataFrame final:")
print(df)