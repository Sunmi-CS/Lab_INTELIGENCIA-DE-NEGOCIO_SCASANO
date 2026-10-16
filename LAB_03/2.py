import pandas as pd
import numpy as np

datos = {
  "Ingreso" : [1000.0, 1200.0, np.nan, 1400.0, 5000.0]
}

df = pd.DataFrame(datos)

print(df.isnull().sum())

mediana = df["Ingreso"].median()
df["Ingreso"] = df["Ingreso"].fillna(mediana)

print(df)
