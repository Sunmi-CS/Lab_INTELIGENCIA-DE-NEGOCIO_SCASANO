ventas <- read.csv("ventas_empresa.csv")

head(ventas)

cat("Cantidad de filas:", nrow(ventas), "\n")
cat("Cantidad de columnas:", ncol(ventas), "\n")
cat("Cantidad de valores nulos:", sum(is.na(ventas)), "\n")

cantidad_producto <- aggregate(
  Cantidad ~ Producto,
  data = ventas,
  sum
)

par(
  mar = c(12, 5, 4, 2),
  mgp = c(3.5, 1, 0)
)

barplot(
  cantidad_producto$Cantidad,
  names.arg = cantidad_producto$Producto,
  main = "Cantidad vendida por producto",
  xlab = "Producto",
  ylab = "Cantidad vendida",
  col = "steelblue",
  border = "white",
  las = 2,
  cex.names = 0.8
)

