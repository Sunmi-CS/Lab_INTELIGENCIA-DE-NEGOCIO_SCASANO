import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
df = pd.read_csv('aids_clinical-7.csv', sep=';')
X = df[['preanti']]
y = df['str2']
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.15,
    random_state=42
)
modelo = LinearRegression()
modelo.fit(X_train, y_train)
y_pred = modelo.predict(X_train)
r2 = r2_score(y_train, y_pred)
print("REGRESIÓN LINEAL SIMPLE")
print("-----------------------------")
print("Total de registros:", len(df))
print("Datos de entrenamiento:", len(X_train))
print("Datos de prueba:", len(X_test))

print("\nRESULTADOS DEL MODELO")
print("Intercepto:", modelo.intercept_)
print("Coeficiente:", modelo.coef_[0])
print("R2 Score (Train):", r2)