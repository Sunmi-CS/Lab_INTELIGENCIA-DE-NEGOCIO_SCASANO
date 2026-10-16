ventas <- read.csv("ventas.csv")

ventas$Importe <- ventas$Cantidad * ventas$Precio

print(ventas)