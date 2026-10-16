producto = input("Ingrese el nombre del nuevo producto: ")

with open("P02_inventario.txt", "a", encoding="utf-8") as archivo:
    archivo.write(producto + "\n")

with open("P02_inventario.txt", "r", encoding="utf-8") as archivo:
    productos = archivo.readlines()

print("\nlista actualizada de productos:")

for producto in productos:
    print(producto.strip())