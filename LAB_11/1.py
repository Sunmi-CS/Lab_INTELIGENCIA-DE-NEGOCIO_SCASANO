import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
# 2. Crear los datos
data = {"Edad": [22, 25, 30, 35, 40, 45, 23, 28, 32, 38, 50, 26],
    "Ingresos_Mensuales": [1200, 1500, 2500, 3000, 3500, 4000,
                           1000, 1800, 2700, 3200, 4500, 1400],
    "Deuda_Mensual": [800, 700, 600, 900, 1200, 1800,
                      850, 1100, 700, 1500, 2200, 1000],
    "Riesgo": [1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1]}
df = pd.DataFrame(data)
# 3. Separar variables predictoras y objetivo
X = df[["Edad", "Ingresos_Mensuales", "Deuda_Mensual"]]
y = df["Riesgo"]
# 4. Dividir los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42, stratify=y
)
# 5. Crear el modelo Random Forest
modelo = RandomForestClassifier(
    n_estimators=100, random_state=42 )
# 6. Entrenar el modelo
modelo.fit(X_train, y_train)
# 7. Realizar predicciones
y_pred = modelo.predict(X_test)
# 8. Evaluar el modelo usando Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Predicciones:", y_pred)
print("Valores reales:", list(y_test))
print("Accuracy:", round(accuracy, 4))
# 9. Mostrar matriz de confusión
print("\nMatriz de confusión:")
print(confusion_matrix(y_test, y_pred))