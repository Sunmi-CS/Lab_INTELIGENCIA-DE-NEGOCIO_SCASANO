import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, roc_auc_score
from lightgbm import LGBMClassifier

df = pd.read_csv("03_tienda_online_compra.csv")
print("Primeras filas:")
print(df.head())
X = df.drop(["compro", "id_usuario"], axis=1)
y = df["compro"]

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
    n_estimators=250,
    learning_rate=0.04,
    max_depth=5,
    random_state=42,
    verbosity=-1
)
modelo.fit(X_train, y_train)
y_pred = modelo.predict(X_test)
y_proba = modelo.predict_proba(X_test)[:, 1]

print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("AUC:", roc_auc_score(y_test, y_proba))

importancia = pd.DataFrame({
    "variable": X_train.columns,
    "importancia": modelo.feature_importances_
})
importancia = importancia.sort_values(
    "importancia",
    ascending=False
)
top_10 = importancia.head(10)

print("\nTop 10 variables más importantes:")
print(top_10.to_string(index=False))

top_10_grafica = top_10.sort_values(
    "importancia",
    ascending=True
)
plt.figure(figsize=(10, 6))
plt.barh(
    top_10_grafica["variable"],
    top_10_grafica["importancia"],
    color="steelblue"
)
plt.xlabel("Importancia")
plt.ylabel("Variables")
plt.title("Top 10 variables importantes - LightGBM")
plt.grid(axis="x", alpha=0.3)
plt.tight_layout()
plt.show()
