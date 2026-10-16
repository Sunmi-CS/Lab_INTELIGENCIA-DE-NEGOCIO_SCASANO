import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from scipy.stats import pearsonr
import matplotlib.pyplot as plt

# 1. IMPORTAR EL ARCHIVO
df = pd.read_excel("productividad.xlsx")
print("===== PRIMEROS REGISTROS =====")
print(df)

# 2. DEFINIR VARIABLES
X = df[["Horas_Capacitacion"]]
y = df["Productividad"]

# 3. MODELO DE REGRESIÓN
modelo = LinearRegression()
modelo.fit(X, y)
intercepto = modelo.intercept_
pendiente = modelo.coef_[0]
y_pred = modelo.predict(X)

# 4. CORRELACIÓN DE PEARSON
r, p_valor = pearsonr(
    df["Horas_Capacitacion"],
    df["Productividad"]
)

# 5. COEFICIENTE R²
r2 = r2_score(y, y_pred)

# 6. RESULTADOS
print("\n===== RESULTADOS =====")
print(f"Intercepto: {intercepto:.5f}")
print(f"Pendiente: {pendiente:.5f}")
print(
    f"Ecuación de regresión: "
    f"y = {intercepto:.5f} + {pendiente:.5f}x"
)
print(f"Coeficiente de Pearson (r): {r:.5f}")
print(f"Coeficiente de determinación (R²): {r2:.5f}")
print(f"R² en porcentaje: {r2 * 100:.2f}%")

# 7. GRÁFICO
plt.figure(figsize=(9, 6))
plt.scatter(
    df["Horas_Capacitacion"],
    df["Productividad"],
    color="blue",
    label="Datos reales"
)
plt.plot(
    df["Horas_Capacitacion"],
    y_pred,
    color="red",
    linewidth=2,
    label="Recta de regresión"
)
plt.xlabel("Horas de capacitación")
plt.ylabel("Productividad (unidades producidas semanalmente)")
plt.title("Horas de capacitación vs. productividad")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()