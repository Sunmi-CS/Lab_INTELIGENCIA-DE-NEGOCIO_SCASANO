
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree

datos = {
    "Libros pendientes": [0, 1, 2, 3],
    "Dias de retraso": [0, 0, 5, 8],
    "Prestamo": [
        "Permitido", "Permitido", "No permitido", "No permitido"
    ]
}
df = pd.DataFrame(datos)
print("Datos de préstamos:")
print(df)
X = df[["Libros pendientes", "Dias de retraso"]]
y = df["Prestamo"]
modelo = DecisionTreeClassifier(random_state=42)
modelo.fit(X, y)
nuevo_prestamo = pd.DataFrame({
    "Libros pendientes": [2],
    "Dias de retraso": [6]
})
prediccion = modelo.predict(nuevo_prestamo)
print("\nPredicción del préstamo:", prediccion[0])
plt.figure(figsize=(12, 7))
plot_tree(
    modelo,
    feature_names=["Libros pendientes", "Dias de retraso"],
    class_names=modelo.classes_,
    filled=True,
    rounded=True
)
plt.title("Árbol de decisión para préstamos de biblioteca")
plt.show()