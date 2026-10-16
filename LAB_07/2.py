import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from scipy.stats import pearsonr
import matplotlib.pyplot as plt

# 1. DATOS
publicidad = np.array([2, 4, 6, 8, 10, 12, 14, 16])
ventas = np.array([18, 25, 31, 39, 44, 51, 57, 64])
X = publicidad.reshape(-1, 1)
y = ventas

# 2. MODELO DE REGRESIÓN
modelo = LinearRegression()
modelo.fit(X, y)
intercepto = modelo.intercept_
pendiente = modelo.coef_[0]
y_pred = modelo.predict(X)

# 3. CORRELACIÓN DE PEARSON
r, p_valor = pearsonr(publicidad, ventas)

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
plt.scatter(publicidad, ventas, color="blue", label="Datos reales")
plt.plot(publicidad, y_pred, color="red", linewidth=2, label="Recta de regresión")

plt.xlabel("Publicidad (miles de S/)")
plt.ylabel("Ventas (miles de S/)")
plt.title("Inversión en publicidad vs. ventas")
plt.legend()
plt.grid(True)
plt.savefig("grafico_2.png", dpi=110)
plt.show()
