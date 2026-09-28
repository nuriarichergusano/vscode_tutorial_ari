# Script de práctica Python
# Ejecuta cada celda con Shift+Enter (requiere la extensión Python/Jupyter)


import pandas as pd
import matplotlib.pyplot as plt

# %% 1. Un dataframe sencillo
df = pd.DataFrame({
    "mes": ["Enero", "Febrero", "Marzo", "Abril"],
    "temperatura": [4.2, 5.8, 9.1, 12.4],
    "precipitacion": [45, 38, 52, 60],
})

# %% 2. Verlo en la consola
print(df)

# %% 3. Abrir el Data Viewer (Variable Explorer de VS Code)
# Con la extensión Python: pestaña "Jupyter: Variables" o clic derecho > "View Value in Data Viewer"

# %% 4. Alguna transformación básica
df["temperatura_f"] = df["temperatura"] * 9 / 5 + 32
print(df)

# %% 5. Un resumen rápido
print(df.describe())

# %% 6. Gráfico para ver el panel de Plots
plt.bar(df["mes"], df["temperatura"])
plt.title("Temperatura por mes")
plt.ylabel("ºC")
plt.show()
