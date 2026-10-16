import pandas as pd
tienda = pd.read_csv("P09_tienda_kdd.csv")

print("Valores faltantes por columna:")
print(tienda.isnull().sum())

duplicados = tienda.duplicated().sum()
print("\nCantidad de registros duplicados:", duplicados)

tienda = tienda.drop_duplicates()
media_cantidad = tienda["Cantidad"].mean()
mediana_precio = tienda["Precio"].median()

tienda["Cantidad"] = tienda["Cantidad"].fillna(media_cantidad)
tienda["Precio"] = tienda["Precio"].fillna(mediana_precio)

print("\nDataset después de limpiar:")
print(tienda)