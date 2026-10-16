import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree

datos = pd.DataFrame({
    "Sesiones asistidas": [1, 2, 4, 5],
    "Tareas entregadas": [0, 1, 3, 4],
    "Participación": ["Baja", "Baja", "Alta", "Alta"]
})

print("DataFrame:")
print(datos)

X = datos[["Sesiones asistidas", "Tareas entregadas"]]
y = datos["Participación"]

arbol = DecisionTreeClassifier(max_depth=3, random_state=42)
arbol.fit(X, y)

nuevo = pd.DataFrame({
    "Sesiones asistidas": [4],
    "Tareas entregadas": [4]
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

plt.title("Árbol de decisión: participación del estudiante")
plt.show()
