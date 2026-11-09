import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_absolute_error, r2_score
df = pd.read_csv('breast_wisconsin-7.csv', sep=';')
X = df.drop(columns=['COD_identificacion_dni', 'fractal_dimension3'])
y = df['fractal_dimension3']
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.30,
    random_state=42
)
modelo = make_pipeline(
    SimpleImputer(strategy='median'),
    RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )
)
modelo.fit(X_train, y_train)
y_pred = modelo.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("EVALUACION DEL MODELO - RANDOM FOREST REGRESSOR")
print("-----------------------------------------------")
print("Total de registros:", len(df))
print("Datos de entrenamiento:", len(X_train))
print("Datos de prueba:", len(X_test))
print("\nMETRICAS DE EVALUACION (TEST)")
print("MAE:", round(mae, 6))
print("R2 Score:", round(r2, 4))