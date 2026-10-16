import pandas as pd
import matplotlib.pyplot as plt

ventas = pd.read_csv("P06_ventas_tienda.csv")

total_ventas = ventas.groupby("Producto")["Cantidad"].sum()

print("cantidad total vendida por producto:")
print(total_ventas)

producto_mayor = total_ventas.idxmax()
cantidad_mayor = total_ventas.max()

print("\nProducto con mayor cantidad vendida:", producto_mayor)
print("cantidad vendida:", cantidad_mayor)

total_ventas.plot(kind="bar")

plt.title("cantidad vendida por producto")
plt.xlabel("producto")
plt.ylabel("cantidad vendida")
plt.show()