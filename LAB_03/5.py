import pandas as pd
import numpy as np

# Crear dataset
df = pd.DataFrame({
    "Producto": ["Laptop", "Mouse", "Teclado", "Laptop",
                 "Monitor", "Mouse", "Teclado", "Laptop"],
    "Cantidad": [2, 5, 3, np.nan, 2, 4, 6, 2],
    "Precio": [2500, 60, 120, 2500, 800, np.nan, 120, 2500]
})

# Tabla inicial
print("TABLA INICIAL")
print(df)

# Valores faltantes
print("\nVALORES FALTANTES")
print(df.isnull().sum())

# Mostrar duplicados
print("\nREGISTROS DUPLICADOS")
print(df[df.duplicated(keep=False)])

# Eliminar duplicados
df = df.drop_duplicates()
print("\nTABLA SIN DUPLICADOS")
print(df)

# Reemplazar valores faltantes
moda_cantidad = df["Cantidad"].mode()[0]
df["Cantidad"] = df["Cantidad"].fillna(moda_cantidad)

mediana_precio = df["Precio"].median()
df["Precio"] = df["Precio"].fillna(mediana_precio)

print("\nTABLA SIN VALORES FALTANTES")
print(df)

# Agrupar por producto y sumar cantidades
df_final = df.groupby("Producto", as_index=False).agg({
    "Cantidad": "sum",
    "Precio": "first"
})

# Tabla final
print("\nTABLA FINAL LIMPIA")
print(df_final)
