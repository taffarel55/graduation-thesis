import matplotlib.pyplot as plt
import csv
import numpy as np

file = "default_representative_100"

x_values = []
y_values = []

with open(f"data/{file}.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        x_values.append(float(row[0]))
        y_values.append(float(row[1]))

# Calcula o seno de x_values
y_sen = np.sin(x_values)

# Calcula as diferenças entre y_values e y_sen
diferencas = np.array(y_values) - y_sen

# Calcula o desvio padrão das diferenças
desvio_padrao = np.std(diferencas)

# Calcula o erro máximo absoluto
erro_maximo = np.max(np.abs(diferencas))

# Calcula o erro máximo relativo
erro_maximo_relativo = erro_maximo / np.max(np.abs([y_sen, y_values]))

# Plotagem do gráfico
plt.plot(x_values, y_sen, "b.", label="Senoide")
plt.plot(x_values, y_values, "r.", label="Predição")
plt.legend(fontsize="large")

# Exibição do gráfico
plt.show()

# Exibição do desvio padrão
print(f"Desvio Padrão: {desvio_padrao}")

# Exibição do erro máximo
print(f"Erro Máximo: {erro_maximo}")
