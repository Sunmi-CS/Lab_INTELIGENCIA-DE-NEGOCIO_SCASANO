import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import numpy as np
# 2. Crear los datos
data = {
    "Personas": [1, 2, 3, 4, 5, 2, 3, 4, 5, 6, 1, 3],
    "Electrodomesticos": [4, 5, 7, 8, 10, 6, 8, 9, 11, 12, 3, 6],
    "Horas_Uso_Diario": [3, 4, 5, 6, 7, 5, 6, 7, 8, 9, 2, 4],
    "Consumo_kWh": [80, 120, 180, 240, 310, 150, 220, 280, 350, 420, 60, 160]}
df = pd.DataFrame(data)
# 3. Separar variables predictoras y objetivo
X = df[["Personas", "Electrodomesticos", "Horas_Uso_Diario"]]
y = df["Consumo_kWh"]
# 4. Dividir los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42)
# 5. Crear el modelo Random Forest Regressor
modelo = RandomForestRegressor(
    n_estimators=100, random_state=42)
# 6. Entrenar el modelo
modelo.fit(X_train, y_train)
# 7. Realizar predicciones
y_pred = modelo.predict(X_test)
# 8. Evaluar el modelo usando MSE y RMSE
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
print("Predicciones:", y_pred)
print("Valores reales:", list(y_test))
print("MSE:", round(mse, 4))
print("RMSE:", round(rmse, 4))