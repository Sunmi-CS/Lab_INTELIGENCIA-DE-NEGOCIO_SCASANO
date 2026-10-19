import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, roc_auc_score, classification_report
from lightgbm import LGBMClassifier

df = pd.read_csv("04_salud_riesgo.csv")
print("Primeras filas de la base de datos:")
print(df.head())
print("\nValores nulos por columna:")
print(df.isnull().sum())
X = df.drop("riesgo_alto", axis=1)
y = df["riesgo_alto"]

variables_numericas = X.select_dtypes(
    include=["number"]
).columns

variables_categoricas = X.select_dtypes(
    include=["object", "category", "bool"]
).columns

for col in variables_numericas:
    X[col] = X[col].fillna(X[col].median())

for col in variables_categoricas:
    if X[col].isnull().any() and not X[col].mode().empty:
        X[col] = X[col].fillna(X[col].mode()[0])

X = pd.get_dummies(X, drop_first=True, dtype=int)
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.30,
    random_state=42,
    stratify=y
)
modelo = LGBMClassifier(
    n_estimators=300,
    learning_rate=0.05,
    max_depth=5,
    random_state=42,
    verbosity=-1
)
modelo.fit(X_train, y_train)
y_pred = modelo.predict(X_test)
y_proba = modelo.predict_proba(X_test)[:, 1]
print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("AUC:", roc_auc_score(y_test, y_proba))
print("\nReporte de clasificación:")
print(classification_report(y_test, y_pred))