def mostrar_estudiantes(ruta_archivo):
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            estudiantes = [linea.strip() for linea in archivo if linea.strip()]

        print("Lista de estudiantes registrados:")
        print("-" * 35)

        for numero, nombre in enumerate(estudiantes, start=1):
            print(f"{numero}. {nombre}")

        print("-" * 35)
        print(f"Total de estudiantes: {len(estudiantes)}")

    except FileNotFoundError:
        print(f"Error: no se encontró el archivo '{ruta_archivo}'.")


if __name__ == "__main__":
    mostrar_estudiantes("estudiantes.txt")
