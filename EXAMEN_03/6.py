import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score
df = pd.read_csv('aids_clinical-7.csv', sep=';')
X = df.drop(columns=['str2'])
y = df['str2']
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.20,
    random_state=42,
    stratify=y
)
modelo = make_pipeline(
    SimpleImputer(strategy='median'),
    StandardScaler(),
    LogisticRegression(max_iter=1000)
)
modelo.fit(X_train, y_train)
y_pred = modelo.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred, zero_division=0)
print("EVALUACION DEL MODELO - REGRESION LOGISTICA")
print("--------------------------------------------")
print("Total de registros:", len(df))
print("Datos de entrenamiento:", len(X_train))
print("Datos de prueba:", len(X_test))
print("\nMETRICAS DE EVALUACION (TEST)")
print("Accuracy:", round(accuracy, 4))
print("F1-score:", round(f1, 4))
print("\nRESULTADOS EN PORCENTAJE")
print("Accuracy:", round(accuracy * 100, 2), "%")
print("F1-score:", round(f1 * 100, 2), "%")