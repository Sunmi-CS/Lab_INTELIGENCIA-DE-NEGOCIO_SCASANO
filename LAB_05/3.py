import pandas as pd
import numpy as np

datos = {
    "Estudiantes": ["Luis", "Carlos", "María", "José", "Lucía", "Pedro"],
    "Nota": [12, np.nan, 18, 14, np.nan, 16]
}

df = pd.DataFrame(datos)
print("Datos originales:")
print(df)

# a) Media de las notas disponibles
media = df["Nota"].mean()
print("\nMedia de las notas disponibles:", media)

# b) Reemplazar NaN por la media
df["Nota"] = df["Nota"].fillna(media)
print("\nDataFrame final:")
print(df)
