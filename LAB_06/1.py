import pandas as pd
import numpy as np

datos = pd.DataFrame({
    "Estudiante": ["Ana", "Luis", "Marta", "José"],
    "Horas de estudio": [3, 2, 4, 1],
    "Asistencia (%)": [85, np.nan, 90, 60],
    "Resultado": ["Aprueba", "No aprueba", "Aprueba", "No aprueba"]
})

print("DataFrame:")
print(datos)

print("\nNúmero de filas:", datos.shape[0])
print("Número de columnas:", datos.shape[1])

print("\nDatos faltantes por columna:")
print(datos.isnull().sum())

estudiante_faltante = datos.loc[datos.isnull().any(axis=1), "Estudiante"]

print("\nEstudiante con dato faltante:")
print(estudiante_faltante.to_string(index=False))
