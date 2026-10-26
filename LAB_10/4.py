import pandas as pd
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import (precision_score,
    recall_score, f1_score, confusion_matrix, classification_report)
from sklearn.pipeline import make_pipeline
# 1. SIMULAR 650 REGISTROS
X, y = make_classification(
    n_samples=650, n_features=8,
    n_informative=5, n_redundant=1,
    n_repeated=0, n_classes=2,
    weights=[0.65, 0.35], random_state=29)
# Crear nombres para las ocho variables
columnas = ["variable_1", "variable_2", "variable_3",
    "variable_4", "variable_5", "variable_6",
    "variable_7", "variable_8"]
df = pd.DataFrame(X, columns=columnas)
df["cancelacion"] = y
print("PRIMEROS REGISTROS:")
print(df.head())
print("\nDISTRIBUCIÓN DE CLASES:")
print(df["cancelacion"].value_counts())
print(df["cancelacion"].value_counts(normalize=True).round(3))
# 2. SEPARAR VARIABLES PREDICTORAS Y OBJETIVO
X = df[columnas]
y = df["cancelacion"]
# 3. DIVIDIR EN ENTRENAMIENTO Y PRUEBA
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=29, stratify=y)
print("\nTAMAÑO DE LOS CONJUNTOS:")
print("Entrenamiento:", len(X_train))
print("Prueba:", len(X_test))
# 4. CREAR PIPELINE CON ESCALAMIENTO Y SVM-RBF
modelo = make_pipeline(
    StandardScaler(), SVC( kernel="rbf", C=1,
        gamma="scale" ))
# 5. ENTRENAR EL MODELO
modelo.fit(X_train, y_train)
# 6. REALIZAR PREDICCIONES
y_pred = modelo.predict(X_test)
# 7. CALCULAR MÉTRICAS
precision = precision_score(y_test, y_pred, pos_label=1, zero_division=0)
recall = recall_score(y_test, y_pred, pos_label=1, zero_division=0)
f1 = f1_score(y_test, y_pred, pos_label=1, zero_division=0)
# 8. MATRIZ DE CONFUSIÓN
cm = confusion_matrix(y_test, y_pred, labels=[0, 1])
tabla_cm = pd.DataFrame(cm,
    index=["Real: No cancela (0)", "Real: Cancela (1)"],
    columns=["Predicho: No cancela (0)", "Predicho: Cancela (1)"])
print("\nMATRIZ DE CONFUSIÓN:")
print(tabla_cm)
print("\nMÉTRICAS DEL MODELO:")
print(f"Precisión: {precision:.3f}")
print(f"Recall:    {recall:.3f}")
print(f"F1-score:  {f1:.3f}")
# 9. IDENTIFICAR FALSOS NEGATIVOS
# Falso negativo: el usuario cancela, pero el modelo predice 0.
falsos_negativos = ((y_test == 1) & (y_pred == 0))
indices_fn = y_test.index[falsos_negativos]
print("\nFALSOS NEGATIVOS:")
print("Cantidad:", int(falsos_negativos.sum()))
if len(indices_fn) > 0:
    detalle_fn = df.loc[indices_fn, columnas + ["cancelacion"]].copy()
    detalle_fn["prediccion"] = 0
    print(detalle_fn)
else:
    print("No se detectaron falsos negativos en el conjunto de prueba.")
# 10. VERIFICAR UMBRALES DE ACEPTACIÓN
umbral_recall = 0.75
umbral_precision = 0.60
cumple_recall = recall >= umbral_recall
cumple_precision = precision >= umbral_precision
print("\nVERIFICACIÓN DE UMBRALES:")
print(f"Recall >= {umbral_recall:.2f}:",
    "CUMPLE" if cumple_recall else "NO CUMPLE")
print(f"Precisión >= {umbral_precision:.2f}:",
    "CUMPLE" if cumple_precision else "NO CUMPLE")
# 11. DECISIÓN AUTOMÁTICA
if cumple_recall and cumple_precision: decision = "aprobar preliminarmente"
else:
    decision = "ajustar el modelo"
print("\nDECISIÓN AUTOMÁTICA:")
print(decision)
# 12. ADVERTENCIA ANTES DEL DESPLIEGUE
print("\nADVERTENCIA:")
print("Antes del despliegue, revisar sesgos, posibles fugas de información, "
    "estabilidad de las métricas y utilidad para el negocio. "
    "La aprobación es preliminar y no garantiza un buen rendimiento futuro.")