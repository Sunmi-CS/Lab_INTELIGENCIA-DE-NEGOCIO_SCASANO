import pandas as pd
from sklearn.impute import KNNImputer

df = pd.read_excel("datos_imputacion_knn_5_vecinos.xlsx")
print("Datos originales:")
print(df)

knn_imputer = KNNImputer(n_neighbors=5)
columnas = ["Trabajadores", "Horas_Funcionamiento", "Consumo_kWh"]
df[columnas] = knn_imputer.fit_transform(df[columnas])

df = df.round(2)
print("\nDataFrame después de la imputación:")
print(df)