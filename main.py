import subprocess
import time
import random
import matplotlib.pyplot as plt

num_tests = 100
message_sizes = [2, 5, 7]  # Vary the message sizes
error_probabilities = [0.01, 0.05, 0.1]  # Vary the error probabilities
algorithm_options = [1, 2]  # Vary the algorithm options

results = []

total_time = 0
for size in message_sizes:
  for error_prob in error_probabilities:
    for _ in range(num_tests):
        random_choice = random.choice(algorithm_options)
        start_time = time.time()
        subprocess.run(["javac", "socketEmisor2.java"])
        subprocess.run(["java", "socketEmisor2", str(size), str(error_prob), str(random_choice)])
        end_time = time.time()

        total_time += end_time - start_time

        avg_time = total_time / num_tests
        results.append((size, error_prob, random_choice, avg_time))

errorHamming = 0
errorCRC = 0

# Leer el archivo 'errores.txt'
with open('errores.txt', 'r') as archivo:
    lineas = archivo.readlines()

resultados = []
for linea in lineas:
    if 'No error' in linea:
        resultados.append(0)
    else:
        resultados.append(1)


final = []
final2 = []

for i, result in enumerate(results):

  size, error_prob, random_choice, avg_time = result
  was_error = resultados[i]

  if random_choice == 1:
     final.append(("Hamming", was_error))
  else:
      final.append(("CRC", was_error))

  final2.append((size,was_error))

hamming_errors = 0
crc_errors = 0
no_errors = 0

error_count1 = 0
error_count2 = 0
error_count3 = 0
count1 = 0
count2 = 0
count3 = 0

for algo, error_count in final:
    if error_count == 1:
        if algo == 'Hamming':
            hamming_errors += 1
        elif algo == 'CRC':
            crc_errors += 1
    elif error_count == 0:
        no_errors += 1

for size, error_count in final2:
    if error_count == 1:
        if size == 1:
            error_count1 += 1
        elif size == 2:
            error_count2 += 1
        elif size == 3:
            error_count3 += 1
    elif error_count == 0:
        if size == 1:
            count1 += 1
        elif size == 2:
            count2 += 1
        elif size == 3:
            count3 += 1
    
    

algorithms = ['Hamming', 'CRC', 'Sin Error']
error_counts = [hamming_errors, crc_errors, no_errors]
plt.bar(algorithms, error_counts)
plt.xlabel('Algoritmo de Detección de Errores')
plt.ylabel('Cantidad de Casos')
plt.title('Errores y Casos Sin Error por Algoritmo')
plt.show()



message_sizes = ['1', '2', '3']
error_counts = [error_count1, error_count2, error_count3]
no_error_counts = [count1, count2, count3]

# Convertir los valores de error_counts y no_error_counts a enteros si no lo están
error_counts = list(map(int, error_counts))
no_error_counts = list(map(int, no_error_counts))

# Crear la gráfica
plt.figure(figsize=(10, 6))
plt.bar(message_sizes, error_counts, label='Errores')
plt.bar(message_sizes, no_error_counts, bottom=error_counts, label='Sin Errores')

# Etiquetas y título
plt.xlabel('Tamaño del Mensaje')
plt.ylabel('Cantidad')
plt.title('Cantidad de Errores y Sin Errores por Tamaño de Mensaje')
plt.legend()

# Mostrar la gráfica
plt.show()



archivo_ruta = "errores.txt"

with open(archivo_ruta, "r+") as archivo:
    archivo.truncate(0)
