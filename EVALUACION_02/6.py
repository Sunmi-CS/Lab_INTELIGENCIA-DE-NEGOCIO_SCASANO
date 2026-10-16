import pandas as pd

datos = {
    "Pedido": ["P1", "P2", "P3", "P4", "P5"],
    "Distancia (km)": [2, 5, 8, 12, 6],
    "Lluvia": [0, 0, 1, 1, 0],
    "Entrega": ["A tiempo", "A tiempo", "Con retraso",
                "Con retraso", "A tiempo"]
}
df = pd.DataFrame(datos)

print("DataFrame de pedidos:")
print(df)
print("\nDistancia mínima:", df["Distancia (km)"].min(), "km")
print("Distancia máxima:", df["Distancia (km)"].max(), "km")
print("Distancia promedio:", df["Distancia (km)"].mean(), "km")
conteo = df["Entrega"].value_counts()
print("\nCantidad de pedidos por estado:")
print("A tiempo:", conteo.get("A tiempo", 0))
print("Con retraso:", conteo.get("Con retraso", 0))