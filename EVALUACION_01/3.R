trabajadores <- read.csv("P03_trabajadores.csv")

promedio <- mean(trabajadores$Sueldo)

cat("Sueldo promedio:", promedio, "\n")

posicion <- which.max(trabajadores$Sueldo)

cat("Trabajador con mayor sueldo:",
    trabajadores$Nombre[posicion], "\n")

cat("Mayor sueldo:",
    trabajadores$Sueldo[posicion], "\n")
