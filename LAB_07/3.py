import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from scipy.stats import pearsonr
import matplotlib.pyplot as plt

# 1. DATOS
temperatura = np.array([20, 22, 24, 26, 28, 30, 32, 34])
consumo = np.array([30, 34, 39, 43, 50, 54, 61, 65])
X = temperatura.reshape(-1, 1)
y = consumo

# 2. MODELO DE REGRESIÓN
modelo = LinearRegression()
modelo.fit(X, y)
intercepto = modelo.intercept_
pendiente = modelo.coef_[0]
y_pred = modelo.predict(X)

# 3. CORRELACIÓN DE PEARSON
r, p_valor = pearsonr(temperatura, consumo)

# 4. COEFICIENTE R²
r2 = r2_score(y, y_pred)

# 5. RESULTADOS
print("===== RESULTADOS =====")
print(f"Intercepto: {intercepto:.5f}")
print(f"Pendiente: {pendiente:.5f}")
print(
    f"Ecuación de regresión: "
    f"y = {intercepto:.5f} + ({pendiente:.5f})x"
)
print(f"Coeficiente de Pearson (r): {r:.5f}")
print(f"Coeficiente de determinación (R²): {r2:.5f}")
print(f"R² en porcentaje: {r2 * 100:.2f}%")

# 6. GRÁFICO
plt.scatter(temperatura, consumo, color="blue", label="Datos reales")
plt.plot(temperatura, y_pred, color="red", linewidth=2, label="Recta de regresión")

plt.xlabel("Temperatura (°C)")
plt.ylabel("Consumo de energía (kWh)")
plt.title("Temperatura vs. consumo de energía")
plt.legend()
plt.grid(True)
plt.savefig("grafico_3.png", dpi=110)
plt.show()
