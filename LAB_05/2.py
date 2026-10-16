import pandas as pd
import matplotlib.pyplot as plt

# a) Crear el DataFrame con las edades
edades = [22, 25, 27, 28, 30, 31, 32, 34, 35, 36, 38, 40, 42, 45, 48]
df = pd.DataFrame({"Edad": edades})
print("DataFrame de edades:")
print(df)

# Histograma con 5 intervalos (bins)
plt.figure(figsize=(8, 5))
plt.hist(df["Edad"], bins=5, color="seagreen", edgecolor="black")
plt.title("Distribución de las edades de los trabajadores")
plt.xlabel("Edad")
plt.ylabel("Frecuencia")
plt.show()

