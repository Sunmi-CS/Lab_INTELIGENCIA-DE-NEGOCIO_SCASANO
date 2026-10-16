import pandas as pd

datos = pd.DataFrame({
    "Pedido": ["P1", "P2", "P3", "P4", "P5"],
    "Distancia (km)": [2, 4, 8, 10, 6],
    "Lluvia (0 = no, 1 = sí)": [0, 0, 1, 1, 0],
    "Entrega": ["A tiempo", "A tiempo", "Con retraso",
                "Con retraso", "A tiempo"]
})

print("DataFrame:")
print(datos)

print("\nDistancia mínima:", datos["Distancia (km)"].min(), "km")
print("Distancia máxima:", datos["Distancia (km)"].max(), "km")
print("Distancia promedio:", datos["Distancia (km)"].mean(), "km")

print("\nCantidad de pedidos:")
print(datos["Entrega"].value_counts())
