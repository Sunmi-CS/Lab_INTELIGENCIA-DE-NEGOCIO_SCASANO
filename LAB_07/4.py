import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from scipy.stats import pearsonr
import matplotlib.pyplot as plt

# 1. DATOS
antiguedad = np.array([1, 2, 3, 4, 5, 6, 7, 8])
produccion = np.array([98, 94, 91, 85, 82, 76, 73, 68])
X = antiguedad.reshape(-1, 1)
y = produccion

# 2. MODELO DE REGRESIÓN
modelo = LinearRegression()
modelo.fit(X, y)
intercepto = modelo.intercept_
pendiente = modelo.coef_[0]
y_pred = modelo.predict(X)

# 3. CORRELACIÓN DE PEARSON
r, p_valor = pearsonr(antiguedad, produccion)

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
plt.scatter(antiguedad, produccion, color="blue",label="Datos reales")
plt.plot(antiguedad, y_pred, color="red", linewidth=2, label="Recta de regresión")

plt.xlabel("Antigüedad de la máquina (años)")
plt.ylabel("Producción (unidades/hora)")
plt.title("Antigüedad de la máquina vs. producción")
plt.legend()
plt.grid(True)
plt.show()
