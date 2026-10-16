import pandas as pd
import matplotlib.pyplot as plt

# a) Crear el DataFrame
datos = {
    "Producto": ["Laptop", "Mouse", "Teclado", "Monitor", "Audífonos"],
    "Ventas": [35, 80, 55, 42, 68]
}

df = pd.DataFrame(datos)
print("DataFrame de ventas:")
print(df)

# b) Gráfico de barras Producto vs. Ventas
plt.figure(figsize=(8, 5))
plt.bar(df["Producto"], df["Ventas"], color="steelblue")
plt.title("Ventas por Producto")
plt.xlabel("Producto")
plt.ylabel("Ventas")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.show()
