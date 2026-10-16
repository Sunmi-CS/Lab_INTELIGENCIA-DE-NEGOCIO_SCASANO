import pandas as pd

print("\na) DATASET CON COLUMN. IMPORTE" + "="*60)

df_productos = pd.read_csv("productos.csv")

df_productos["Importe"] = df_productos["Cantidad"] * df_productos["Precio"]

print(df_productos)



print("\nb) Agrupar por producto ")

impxproducto = df_productos.groupby("Producto")["Importe"].sum()
print(impxproducto)



producto_top = impxproducto.idxmax()
importe_top = impxproducto.max()
print(f"\nc) El producto con mayor importe total de ventas es: " f"'{producto_top}' con s/. {importe_top:,.2f}")
