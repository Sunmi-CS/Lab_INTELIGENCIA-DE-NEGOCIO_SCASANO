import pandas as pd
import numpy as np

# Base 1: Estudiantes
datos_estudiantes = {
    "Codigo": [1, 2, 3, 4, 5],
    "Nombre": ["Ana", "Luis", "Carlos", "María", "José"],
    "Edad": [20, np.nan, 21, 23, np.nan]
}
df_estudiantes = pd.DataFrame(datos_estudiantes)

# Base 2: Notas
datos_notas = {
    "Codigo": [1, 2, 3, 4, 5],
    "Nota": [15, np.nan, 14, 17, 16],
    "Curso": ["Matemática", "Comunicación", "Matemática", np.nan, "Matemática"]
}
df_notas = pd.DataFrame(datos_notas)


# Unir las dos bases
df_final = pd.merge(df_estudiantes, df_notas, on="Codigo")
print("Base final:")
print(df_final)


# Completar Edad con la MEDIA
media_edad = df_final["Edad"].mean()
print("Media de edad:", media_edad)
df_final["Edad"] = df_final["Edad"].fillna(media_edad)


# Completar Nota con la MEDIANA
mediana_nota = df_final["Nota"].median()
print("Mediana de nota:", mediana_nota)
df_final["Nota"] = df_final["Nota"].fillna(mediana_nota)


# Completar Curso con la MODA
moda_curso = df_final["Curso"].mode()[0]
print("Moda del curso:", moda_curso)
df_final["Curso"] = df_final["Curso"].fillna(moda_curso)


print("Base Final:")
print(df_final)
