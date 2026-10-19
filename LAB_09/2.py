import pandas as pd
df = pd.read_csv("02_colegio_aprobacion.csv")
print("Primeras filas de la base de datos:")
print(df.head())

print("\nValores nulos antes de la limpieza:")
print(df.isnull().sum())

variables_numericas = df.select_dtypes(
    include=["int64", "float64"]
).columns

variables_categoricas = df.select_dtypes(
    include=["object", "category", "bool"]
).columns

for col in variables_numericas:
    df[col] = df[col].fillna(df[col].median())

for col in variables_categoricas:
    if df[col].isnull().any() and not df[col].mode().empty:
        df[col] = df[col].fillna(df[col].mode()[0])

print("\nValores nulos después de la limpieza:")
print(df.isnull().sum())
print("\nTotal de valores nulos:")
print(df.isnull().sum().sum())

print("\nBase de datos limpia:")
print(df.head())
