with open("P01_docentes.txt", "r", encoding="utf-8") as archivo:
    docentes = archivo.readlines()

print("docentes registrados:")

for docente in docentes:
    print(docente.strip())

print("cantidad de docentes:", len(docentes))