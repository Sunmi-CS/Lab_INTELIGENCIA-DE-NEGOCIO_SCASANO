import pandas as pd
pedidos = pd.read_csv("P05_pedidos.csv")

pedidos["Importe"] = pedidos["Cantidad"] * pedidos["Precio"]

print("datos con Importe:")
print(pedidos)

total_producto = pedidos.groupby("Producto")["Importe"].sum()

print("\nimporte total por producto:")
print(total_producto)

producto_mayor = total_producto.idxmax()
importe_mayor = total_producto.max()

print("\nproducto con mayor importe total:", producto_mayor)
print("importe total:", importe_mayor)