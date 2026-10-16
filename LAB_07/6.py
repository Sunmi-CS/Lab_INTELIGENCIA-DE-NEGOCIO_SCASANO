import pandas as pd
import numpy as np

# 1. CREAR LOS DATOS
df = pd.DataFrame({
    "Cliente": ["C01", "C02", "C03", "C04", "C05", "C05", "C06", "C07"],
    "Edad": [25, 32, np.nan, 45, 29, 29, 38, 41],
    "Ingresos": [2500, 3200, 2800, np.nan, 3000, 3000, 4100, 4500],
    "Compras": [4, 6, 5, 8, 4, 4, np.nan, 9],
    "Ciudad": ["Lima", "Arequipa", "Lima", "Cusco",
               "Lima", "Lima", "Arequipa", "Cusco"]
})
print("===== DATOS ORIGINALES =====")
print(df)

# a) VALORES FALTANTES
print("\n===== VALORES FALTANTES =====")
print(df.isnull().sum())

# a) REGISTROS DUPLICADOS
print("\n===== REGISTROS DUPLICADOS =====")
print(df[df.duplicated()])

# b) REEMPLAZAR FALTANTES
df["Edad"] = df["Edad"].fillna(df["Edad"].mean())
df["Ingresos"] = df["Ingresos"].fillna(df["Ingresos"].mean())
df["Compras"] = df["Compras"].fillna(df["Compras"].mean())

# b) ELIMINAR DUPLICADOS
df = df.drop_duplicates()

# c) TRANSFORMAR CIUDAD
df["Ciudad"] = df["Ciudad"].map({
    "Lima": 0,
    "Arequipa": 1,
    "Cusco": 2
})

# DATOS FINALES
print("\n===== CONJUNTO DE DATOS FINAL =====")
print(df)