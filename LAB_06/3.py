import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree

datos = pd.DataFrame({
    "Libros pendientes": [0, 1, 2, 3],
    "Días de retraso": [0, 0, 5, 8],
    "Préstamo": ["Permitido", "Permitido", "No permitido", "No permitido"
    ]
})

print("DataFrame:")
print(datos)

X = datos[["Libros pendientes", "Días de retraso"]]
y = datos["Préstamo"]

arbol = DecisionTreeClassifier(max_depth=3, random_state=42)
arbol.fit(X, y)

nuevo = pd.DataFrame({
    "Libros pendientes": [2],
    "Días de retraso": [6]
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

plt.title("Árbol de decisión: préstamo de libros")
plt.show()
