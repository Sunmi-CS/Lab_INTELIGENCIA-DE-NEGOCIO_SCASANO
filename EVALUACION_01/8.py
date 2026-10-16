import pandas as pd
estudiantes = pd.read_csv("P08_estudiantes.csv")
notas = pd.read_csv("P08_notas.csv")

base = pd.merge(estudiantes, notas, on="Codigo")

print("Base resultante:")
print(base)

promedio = base["Nota"].mean()

print("\nPromedio de las notas:", promedio)