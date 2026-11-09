import pandas as pd
datos = {
    'ID': [1, 2, 3, 4, 5, 6],
    'Nombre': ['Ana', 'Luis', None, 'Marta', 'Pedro', None],
    'Edad': [15, 16, 15, None, 16, 17],
    'Nota': [18, None, 14, 17, None, 15]
}
df = pd.DataFrame(datos)
print("DATAFRAME ORIGINAL")
print(df)
print("\nDATOS FALTANTES")
print(df.isnull().sum())
df['Nombre'] = df['Nombre'].fillna(df['Nombre'].mode()[0])
df['Edad'] = df['Edad'].fillna(df['Edad'].mean())
df['Nota'] = df['Nota'].fillna(df['Nota'].mean())
print("\nDATAFRAME CON DATOS IMPUTADOS")
print(df)
print("\nVERIFICACION DE DATOS FALTANTES")
print(df.isnull().sum())
print("\nTOTAL DE DATOS FALTANTES:")
print(df.isnull().sum().sum())