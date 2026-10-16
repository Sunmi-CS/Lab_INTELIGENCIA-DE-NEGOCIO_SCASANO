import pandas as pd
edades = pd.read_csv("P07_edades.csv")

faltantes = edades["Edad"].isnull().sum()
print("Cantidad de valores faltantes:", faltantes)

media = edades["Edad"].mean()
print("Media de las edades:", media)

edades["Edad"] = edades["Edad"].fillna(media)
print("\nDataset resultante:")
print(edades)