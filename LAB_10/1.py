import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
# 1. CREAR LOS DATOS
data = {
    "edad": [22, 25, 28, 31, 35, 38, 40, 43, 46, 47, 50, 52, 53, 55, 56, 57, 60, 62, 29, 33],
    "ingresos": [1200, 1500, 1800, 1900, 2500, 2700, 3000, 3300, 3500, 3200, 4100, 4000,
                 4300, 4800, 5000, 5100, 5200, 5400, 1600, 2100],
    "deuda": [500, 700, 900, 950, 1200, 1300, 1600, 1700, 1800, 1500, 2300, 2200, 2400,
              2800, 3000, 2900, 3100, 3300, 800, 1000],
    "score_crediticio": [650, 620, 610, 605, 590, 585, 570, 555, 560, 580, 530, 540,
                         520, 510, 500, 505, 490, 480, 615, 600],
    "fuga": [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]
}
df = pd.DataFrame(data)
print("DATOS:")
print(df)
# 2. SEPARAR VARIABLES
X = df[["edad", "ingresos", "deuda", "score_crediticio"]]
y = df["fuga"]
# 3. DIVIDIR DATOS EN ENTRENAMIENTO Y PRUEBA
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y )
# 4. ESCALAR LAS VARIABLES
escalador = StandardScaler()
X_train_escalado = escalador.fit_transform(X_train)
X_test_escalado = escalador.transform(X_test)
# 5. CREAR Y ENTRENAR EL MODELO SVM
modelo_svm = SVC(kernel="linear")
modelo_svm.fit(X_train_escalado, y_train)
# 6. REALIZAR PREDICCIONES
y_pred = modelo_svm.predict(X_test_escalado)
print("\nVALORES REALES:")
print(y_test.tolist())
print("\nVALORES PREDICHOS:")
print(y_pred.tolist())
# 7. CALCULAR EL ACCURACY
accuracy = accuracy_score(y_test, y_pred)
print("\nACCURACY DEL MODELO:")
print(accuracy)
print("\nACCURACY EN PORCENTAJE:")
print(f"{accuracy * 100:.2f}%")