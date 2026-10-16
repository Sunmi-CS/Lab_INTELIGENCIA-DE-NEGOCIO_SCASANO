import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree

datos = {
    "Temperatura": [40, 45, 80, 85],
    "Vibracion": [2, 3, 8, 9],
    "Estado": ["Normal", "Normal", "Revisar", "Revisar"]
}

df = pd.DataFrame(datos)

print("Datos de las máquinas:")
print(df)

X = df[["Temperatura", "Vibracion"]]
y = df["Estado"]

modelo = DecisionTreeClassifier(random_state=42)
modelo.fit(X, y)

nueva_maquina = pd.DataFrame({
    "Temperatura": [82],
    "Vibracion": [8]
})

prediccion = modelo.predict(nueva_maquina)

print("\nPredicción del estado:", prediccion[0])

plt.figure(figsize=(10, 6))

plot_tree(
    modelo,
    feature_names=["Temperatura", "Vibracion"],
    class_names=modelo.classes_,
    filled=True,
    rounded=True
)

plt.title("Árbol de decisión para mantenimiento de máquinas")
plt.show()