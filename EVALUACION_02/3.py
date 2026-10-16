import pandas as pd
import matplotlib.pyplot as plt

datos = {
    "Edad": [20, 22, 25, 27, 28, 30, 31, 32,
             34, 35, 36, 38, 40, 42, 45, 48]
}

df = pd.DataFrame(datos)
print("Edades de los trabajadores:")
print(df)

print("Edad mínima:", df["Edad"].min())
print("Edad máxima:", df["Edad"].max())
print("Edad promedio:", df["Edad"].mean())

plt.hist(df["Edad"], bins=5, edgecolor="black")
plt.title("Histograma de edades de los trabajadores")
plt.xlabel("Edad")
plt.ylabel("Frecuencia")
plt.show()