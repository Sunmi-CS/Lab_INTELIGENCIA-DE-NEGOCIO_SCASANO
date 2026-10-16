import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree

datos = pd.DataFrame({
    "Temperatura (°C)": [40, 45, 80, 85],
    "Vibración": [2, 3, 8, 9],
    "Estado": ["Normal", "Normal", "Revisar", "Revisar"]
})

print("DataFrame:")
print(datos)

X = datos[["Temperatura (°C)", "Vibración"]]
y = datos["Estado"]

arbol = DecisionTreeClassifier(max_depth=3, random_state=42)
arbol.fit(X, y)

nuevo = pd.DataFrame({
    "Temperatura (°C)": [82],
    "Vibración": [8]
})

prediccion = arbol.predict(nuevo)[0]
print("\nPredicción:", prediccion)

plt.figure(figsize=(12, 7))
plot_tree(
    arbol,
    feature_names=X.columns,
    class_names=arbol.classes_,
    filled=True,
    rounded=True,
    impurity=False,
    fontsize=11
)

plt.title("Árbol de decisión: estado de la máquina")
plt.show()
