import pandas as pd
import numpy as np

# Base 1: Estudiantes
datos_estudiantes = {
    "Codigo": [1, 2, 3, 4, 5],
    "Nombre": ["Ana", "Luis", "Carlos", "María", "José"],
    "Edad": [20, np.nan, 21, 23, np.nan]
}
df_estudiantes = pd.DataFrame(datos_estudiantes)

print("Base 1: Estudiantes")
print(df_estudiantes)


# Base 2: Notas
datos_notas = {
    "Codigo": [1, 2, 3, 4, 5],
    "Nota": [15, np.nan, 14, 17, 16],
    "Curso": ["Matemática", "Comunicación", "Matemática", np.nan, "Matemática"]
}
df_notas = pd.DataFrame(datos_notas)

print("Base 2: Notas")
print(df_notas)


# Unir las dos bases mediante Codigo
df_final = pd.merge(df_estudiantes, df_notas, on="Codigo")
print("Base unida:")
print(df_final)
