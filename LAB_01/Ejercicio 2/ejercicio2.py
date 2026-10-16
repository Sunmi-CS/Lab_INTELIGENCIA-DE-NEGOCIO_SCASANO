producto = input("Ingrese el nuevo producto: ")

with open("productos.txt", "a", encoding="utf-8") as archivo:
    archivo.write(producto + "\n")

with open("productos.txt", "r", encoding="utf-8") as archivo:
    productos = archivo.readlines()

print("\nLista actualizada de productos:")

for producto in productos:
    print(producto.strip())