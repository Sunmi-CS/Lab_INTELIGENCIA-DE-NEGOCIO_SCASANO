import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("categorias.csv")

total_ventas = df.groupby("Categoria")["Venta"].sum()

print("Total de ventas por categoría:")
print(total_ventas.to_string())

plt.pie(
    total_ventas,
    labels=total_ventas.index,
    autopct="%1.1f%%"
)

plt.title("Participación de ventas por categoría")
plt.show()

categoria_mayor = total_ventas.idxmax()
venta_mayor = total_ventas.max()

print("\nLa categoría con mayor participación es:",
      categoria_mayor, "con", venta_mayor)
