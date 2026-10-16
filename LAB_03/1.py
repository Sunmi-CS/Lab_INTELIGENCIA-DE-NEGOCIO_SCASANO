import pandas as pd
import numpy as np

datos = {
  "Edad": [18.0, 20, np.nan, 22.0, 24.0]
}

df = pd.DataFrame(datos)

print(df.isnull().sum())

media = df["Edad"].mean()
df["Edad"] = df["Edad"].fillna(media)

print(df)
