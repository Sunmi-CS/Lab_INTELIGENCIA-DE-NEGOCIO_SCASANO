import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
# 2. Crear los datos
data = {
    "Visitas_Mes": [2, 4, 8, 10, 12, 3, 5, 9, 11, 6, 1, 7],
    "Meses_Inscrito": [1, 2, 6, 8, 12, 1, 3, 7, 10, 4, 1, 5],
    "Satisfaccion": [3, 4, 7, 8, 9, 4, 5, 8, 9, 6, 2, 7],
    "Renueva": [0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1]}
df = pd.DataFrame(data)
# 3. Separar variables predictoras y objetivo
X = df[["Visitas_Mes", "Meses_Inscrito", "Satisfaccion"]]
y = df["Renueva"]
# 4. Dividir datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42, stratify=y)
# 5. Crear modelo Random Forest
modelo = RandomForestClassifier(
    n_estimators=100, random_state=42)
# 6. Entrenar el modelo
modelo.fit(X_train, y_train)
# 7. Realizar predicciones
y_pred = modelo.predict(X_test)
# 8. Evaluar el modelo
accuracy = accuracy_score(y_test, y_pred)
print("Predicciones:", y_pred)
print("Valores reales:", list(y_test))
print("Accuracy:", round(accuracy, 4))
# 9. Mostrar matriz de confusión
print("\nMatriz de confusión:")
print(confusion_matrix(y_test, y_pred, labels=[0, 1]))
# 10. Crear un nuevo cliente
nuevo_cliente = pd.DataFrame({"Visitas_Mes": [6],
    "Meses_Inscrito": [5], "Satisfaccion": [7]})
# 11. Predecir si renovará
resultado = modelo.predict(nuevo_cliente)
probabilidad = modelo.predict_proba(nuevo_cliente)[0][1]
print("\nRESULTADOS DEL NUEVO CLIENTE")
print("Clasificación:", resultado[0])
print("Probabilidad de renovación:", round(probabilidad, 4))
# 12. Mostrar decisión
if resultado[0] == 1:
    print("El cliente probablemente SÍ renovará su membresía.")
else:
    print("El cliente probablemente NO renovará su membresía.")