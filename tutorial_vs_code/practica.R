# Script de práctica R
# Ejecuta cada bloque con el cursor en la línea y Ctrl+Enter

# 1. Un dataframe sencillo
df <- data.frame(
  mes = c("Enero", "Febrero", "Marzo", "Abril"),
  temperatura = c(4.2, 5.8, 9.1, 12.4),
  precipitacion = c(45, 38, 52, 60)
)

# 2. Verlo en la consola
print(df)

# 3. Abrir el Data Viewer (como View() en RStudio)
View(df)

# 4. Alguna transformación básica
df$temperatura_f <- df$temperatura * 9 / 5 + 32
View(df)

# 5. Un resumen rápido
summary(df)

# 6. Grafico para ver el panel de Plots
plot(factor(df$mes, levels = df$mes), df$temperatura, main = "Temperatura por mes", ylab = "ºC")
