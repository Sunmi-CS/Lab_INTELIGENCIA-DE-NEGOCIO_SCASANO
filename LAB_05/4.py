import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer

datos = {
    "Estudiante": ["A", "B", "C", "D", "E", "F", "G", "H"],
    "Horas de estudio": [2.0, 3.0, 4.0, 5.0, 6.0, 3.5, 5.5, 4.5],
    "Asistencia (%)": [65, 72, 80, 88, 95, 76, 92, 85],
    "Nota": [10, 12, 14, np.nan, 18, 13, np.nan, 16]
}

df = pd.DataFrame(datos)

print("Datos originales:")
print(df)

knn_imputer = KNNImputer(n_neighbors=3)
columnas = ["Horas de estudio", "Asistencia (%)", "Nota"]

df[columnas] = knn_imputer.fit_transform(df[columnas])
print("\nDatos después de la imputación por KNN:")
print(df)
