import json

def procesar_clientes(ruta_archivo):
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            clientes = json.load(archivo)

        print("Lista de clientes registrados:")
        print("-" * 35)

        for cliente in clientes:
            print(f"Nombre: {cliente['nombre']} | Edad: {cliente['edad']}")

        edades = [cliente["edad"] for cliente in clientes]
        edad_promedio = sum(edades) / len(edades)

        print("-" * 35)
        print(f"Total de clientes: {len(clientes)}")
        print(f"Edad promedio: {edad_promedio:.2f} años")

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{ruta_archivo}'.")

    except json.JSONDecodeError:
        print("Error: El archivo no tiene un formato JSON válido.")


if __name__ == "__main__":
    procesar_clientes("clientes.json")
