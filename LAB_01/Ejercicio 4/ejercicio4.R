empleados <- read.csv("empleados.csv")

sueldo_promedio <- mean(empleados$Sueldo)

indice_mayor <- which.max(empleados$Sueldo)

nombre_mayor <- empleados$Nombre[indice_mayor]
sueldo_mayor <- empleados$Sueldo[indice_mayor]

cat("Sueldo promedio:", sueldo_promedio, "\n")
cat("Trabajador con mayor sueldo:", nombre_mayor, "\n")
cat("Sueldo mayor:", sueldo_mayor, "\n")