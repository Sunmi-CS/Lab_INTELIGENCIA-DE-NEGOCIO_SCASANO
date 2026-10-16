
import pandas as pd
import matplotlib.pyplot as plt

datos = {
    "Producto": ["Impresora", "Laptop", "Monitor", "Teclado", "Mouse"],
    "Cantidad": [25, 40, 30, 65, 90]
}

df = pd.DataFrame(datos)
print("Tabla de productos y cantidades:")
print(df)
plt.bar(df["Producto"], df["Cantidad"])
plt.title("Cantidad de productos vendidos")
plt.xlabel("Producto")
plt.ylabel("Cantidad vendida")
plt.show()