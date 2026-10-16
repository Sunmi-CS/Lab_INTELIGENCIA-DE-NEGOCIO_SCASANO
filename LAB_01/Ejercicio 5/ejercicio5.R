notas <- scan("notas.txt")

promedio <- mean(notas)

nota_maxima <- max(notas)

print(paste("Promedio:", round(promedio, 2)))
print(paste("Nota máxima:", nota_maxima))
