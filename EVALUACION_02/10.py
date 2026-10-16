import pandas as pd

df = pd.read_excel("Pregunta_10_CRISP_DM.xlsx", sheet_name="Datos")
print("DataFrame original:")
print(df)
print("\nValores faltantes por columna:")
print(df.isnull().sum())
df = df.drop_duplicates()
print("\nDataFrame sin duplicados:")
print(df)

columnas_numericas = ["Edad", "Ingresos", "Compras"]

for columna in columnas_numericas:
    df[columna] = df[columna].fillna(df[columna].mean())

df["Ciudad"] = df["Ciudad"].map({
    "Lima": 0,
    "Arequipa": 1,
    "Cusco": 2
})
print("\nDataFrame final:")
print(df.round(2))