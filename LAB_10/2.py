import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (confusion_matrix, classification_report, 
                             precision_score, recall_score, f1_score)
# 1. CREAR LOS DATOS
data = {
    "monto": [ 20, 35, 50, 80, 120, 150, 200, 250, 300, 450, 700, 900, 1200, 
        1500, 1800, 2200, 2500, 3000, 3500, 4000 ],
    "operaciones_dia": [ 1, 1, 2, 2, 3, 2, 4, 3, 5, 6, 8, 10, 12, 
                        15, 18, 20, 22, 25, 28, 30 ],
    "hora_transaccion": [ 9, 10, 11, 12, 14, 15, 16, 18, 19, 20, 21, 
                         22, 23, 0, 1, 2, 3, 4, 5, 6 ],
    "distancia_km": [ 1, 2, 2, 3, 5, 4, 6, 8, 10, 12, 20, 35, 50, 80, 100, 
                     120, 150, 200, 250, 300],
    "fraude": [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ]
}
df = pd.DataFrame(data)
print("DATOS:")
print(df)
# 2. SEPARAR VARIABLES
X = df[ ["monto", "operaciones_dia", "hora_transaccion", "distancia_km"]]
y = df["fraude"]
# 3. DIVIDIR DATOS EN ENTRENAMIENTO Y PRUEBA
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y)
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
# 7. MATRIZ DE CONFUSIÓN
cm = confusion_matrix(y_test, y_pred, labels=[0, 1])
tabla_cm = pd.DataFrame(
    cm,
    index=["Real: Normal (0)", "Real: Fraudulenta (1)"],
    columns=["Predicho: Normal (0)", "Predicho: Fraudulenta (1)"]
)
print("\nMATRIZ DE CONFUSIÓN:")
print(tabla_cm)
# 8. CALCULAR PRECISIÓN, RECALL Y F1-SCORE
precision = precision_score( y_test, y_pred, pos_label=1, zero_division=0)
recall = recall_score( y_test, y_pred, pos_label=1, zero_division=0)
f1 = f1_score( y_test, y_pred, pos_label=1, zero_division=0)
print("\nMÉTRICAS DEL MODELO:")
print(f"Precisión (Precision): {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1-score: {f1:.2f}")
# 9. REPORTE DE CLASIFICACIÓN
print("\nREPORTE DE CLASIFICACIÓN:")
print(classification_report(
    y_test, y_pred, labels=[0, 1], target_names=["Normal", "Fraudulenta"],
    zero_division=0))
