
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_excel("Pregunta_9_Regresion.xlsx", sheet_name="Datos")
df.columns = df.columns.str.strip()

print("Datos de publicidad y ventas:")
print(df)
X = df[["Publicidad (miles de S/)"]]
y = df["Ventas (miles de S/)"]

modelo = LinearRegression()
modelo.fit(X, y)
pendiente = modelo.coef_[0]
intercepto = modelo.intercept_
print("\nEcuación de regresión lineal:")
print(f"Ventas = {intercepto:.4f} + {pendiente:.4f} * Publicidad")

y_pred = modelo.predict(X)
pearson = df["Publicidad (miles de S/)"].corr(
    df["Ventas (miles de S/)"]
)
r2 = modelo.score(X, y)

print("\nCoeficiente de Pearson (r):", round(pearson, 4))
print("Coeficiente de determinación (R²):", round(r2, 4))
print("Porcentaje explicado:", round(r2 * 100, 2), "%")

plt.scatter(X.iloc[:, 0], y, color="blue", label="Datos reales")
plt.plot(X.iloc[:, 0], y_pred, color="red", label="Recta de regresión")

plt.title("Relación entre publicidad y ventas")
plt.xlabel("Publicidad (miles de S/)")
plt.ylabel("Ventas (miles de S/)")
plt.legend()
plt.grid(True)
plt.show()