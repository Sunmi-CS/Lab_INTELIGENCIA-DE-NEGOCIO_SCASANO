import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, f1_score
# 1. CREAR LOS DATOS
data = {
    "temperatura": [60, 62, 65, 67, 70, 72, 75, 78, 80, 82,
        85, 88, 90, 92, 95, 98, 100, 103, 105, 108],
    "presion": [10, 11, 12, 13, 12, 14, 15, 15, 16, 17,
        19, 20, 22, 23, 25, 26, 28, 30, 32, 35],
    "vibracion": [2, 2, 3, 3, 4, 4, 5, 5, 6, 7,
        8, 9, 10, 11, 13, 14, 15, 17, 18, 20],
    "tiempo_produccion": [30, 32, 35, 36, 38, 40, 43, 45, 47, 50,
        55, 58, 60, 63, 66, 70, 75, 78, 80, 85],
    "defectuoso": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1]}
df = pd.DataFrame(data)
print("DATOS:")
print(df)
# 2. SEPARAR VARIABLES
X = df[["temperatura", "presion", "vibracion",
     "tiempo_produccion"]]
y = df["defectuoso"]
# 3. DIVIDIR DATOS EN ENTRENAMIENTO Y PRUEBA
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y)
# 4. ESCALAR LAS VARIABLES
escalador = StandardScaler()
X_train_escalado = escalador.fit_transform(X_train)
X_test_escalado = escalador.transform(X_test)
# 5. DEFINIR LOS TRES MODELOS SVM
modelos = {"Linear": SVC(kernel="linear"),
    "RBF": SVC(kernel="rbf"), "Poly": SVC(kernel="poly", degree=3)}
# 6. ENTRENAR Y EVALUAR LOS MODELOS
resultados = []
for nombre, modelo in modelos.items():
    # Entrenar el modelo
    modelo.fit(X_train_escalado, y_train)
    # Realizar predicciones
    y_pred = modelo.predict(X_test_escalado)
    # Calcular métricas
    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, zero_division=0)
    # Guardar resultados
    resultados.append({"Modelo SVM": nombre, "Accuracy": accuracy,
        "F1-score": f1})
# 7. MOSTRAR TABLA COMPARATIVA
tabla_resultados = pd.DataFrame(resultados)
print("\nTABLA COMPARATIVA DE MODELOS SVM:")
print(tabla_resultados.to_string(
    index=False, formatters={"Accuracy": "{:.2f}".format,
        "F1-score": "{:.2f}".format}))
# 8. IDENTIFICAR EL MODELO CON MAYOR F1-SCORE
mejor_modelo = tabla_resultados.loc[
    tabla_resultados["F1-score"].idxmax()]
print("\nMEJOR MODELO SEGÚN F1-SCORE:")
print(mejor_modelo["Modelo SVM"])
print(f"F1-score: {mejor_modelo['F1-score']:.2f}")