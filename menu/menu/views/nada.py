import pandas as pd

# Crear un DataFrame vacío
df = pd.DataFrame(columns=['columna1', 'columna2'])

# Ejemplo de inserción de datos en el DataFrame
for i in range(10):
    fila = {'columna1': i, 'columna2': i * 2}
    df = df.append(fila, ignore_index=True)

print(df)
