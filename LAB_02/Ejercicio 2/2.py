import pandas as pd

print("\n" + "=" * 60)
print("Ejercicio 2: clientes.csv")

# a) importar al archivo y contar valores nulos por columna
df_clientes = pd.read_csv("clientes.csv")

print ("\na) Valores nulos por columna: ")
print(df_clientes.isnull().sum())


# b) registros duplicados

print ("\n" + "="*60)

n_duplicados = df_clientes.duplicated().sum()
print(f"\nb) Regitro duplicados: {n_duplicados}")


# c) registros que se encuentran duplicados


print ("\n" + "="*60)
print ("\nc) keep=False muestra todas las ocurrencias del registro duplicado")
r_duplicados = df_clientes.duplicated(keep=False)
print(r_duplicados)
