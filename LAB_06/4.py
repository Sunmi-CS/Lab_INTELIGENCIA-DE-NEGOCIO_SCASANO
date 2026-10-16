import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree

datos = pd.DataFrame({
    "Humedad del suelo (%)": [20, 25, 70, 80],
    "Temperatura (°C)": [30, 28, 22, 20],
    "Decisión": ["Regar", "Regar", "No regar", "No regar"]
})

print("DataFrame:")
print(datos)

X = datos[["Humedad del suelo (%)", "Temperatura (°C)"]]
y = datos["Decisión"]

arbol = DecisionTreeClassifier(max_depth=3, random_state=42)
arbol.fit(X, y)

nuevo = pd.DataFrame({
    "Humedad del suelo (%)": [22],
    "Temperatura (°C)": [29]
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

plt.title("Árbol de decisión: riego de cultivos")
plt.show()
