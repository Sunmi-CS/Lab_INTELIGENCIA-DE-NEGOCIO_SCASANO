import pandas as pd

datos = {
    "Producto": ["Laptop", "Mouse", "Teclado", "Monitor", "Audífonos"],
    "Ventas": [45, 80, 60, 35, 70]
}

df = pd.DataFrame(datos)
print(df)
print("Número de filas:", df.shape[0])
print("Número de columnas:", df.shape[1])

total = df["Ventas"].sum()
promedio = df["Ventas"].mean()

print("Ventas totales:", total)
print("Promedio de ventas:", promedio)