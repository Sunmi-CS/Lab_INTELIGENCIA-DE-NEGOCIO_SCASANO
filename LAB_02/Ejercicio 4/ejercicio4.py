import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ventas.csv")

ventas_producto = df.groupby("Producto")["Cantidad"].sum()

print("Cantidad total vendida por producto:")
print(ventas_producto)

producto_mayor = ventas_producto.idxmax()
cantidad_mayor = ventas_producto.max()

print(f"\nEl producto con mayor cantidad vendida es: "
      f"{producto_mayor} ({cantidad_mayor} unidades)")

plt.figure(figsize=(10, 6))
plt.bar(ventas_producto.index, ventas_producto.values, color="steelblue")

plt.title("Cantidad total vendida por producto")
plt.xlabel("Producto")
plt.ylabel("Cantidad vendida")

plt.xticks(rotation=45)

for i, cantidad in enumerate(ventas_producto.values):
    plt.text(i, cantidad + 0.5, str(cantidad),
             ha="center", fontsize=10)

plt.tight_layout()
plt.show()
