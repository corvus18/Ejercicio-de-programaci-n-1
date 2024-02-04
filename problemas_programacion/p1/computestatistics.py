"""
Este codigo calcula estadísticas básicas.
"""

import math
import time

def calculate_mean(data):
    """Calcula Media"""
    return sum(data) / len(data)

def calculate_median(data):
    """Calcula Mediana"""
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 0:
        mid1 = sorted_data[n // 2 - 1]
        mid2 = sorted_data[n // 2]
        return (mid1 + mid2) / 2
    return sorted_data[n // 2]

def calculate_mode(data):
    """Calcula moda"""
    frequency = {}
    for value in data:
        frequency[value] = frequency.get(value, 0) + 1

    max_freq = max(frequency.values())
    mode = [key for key, value in frequency.items() if value == max_freq]
    return mode

def calculate_standard_deviation(data, mean):
    """Calcula Desviacion Estandar"""
    squared_diff = sum((x - mean) ** 2 for x in data)
    variance = squared_diff / len(data)
    return math.sqrt(variance)

def calculate_variance(data, mean):
    """Calcula Varianza"""
    squared_diff = sum((x - mean) ** 2 for x in data)
    return squared_diff / len(data)

def process_file(file_path):
    """Procesa el archivo y devuelve una lista de números"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = []
            for line in file:
                try:
                    number = float(line.strip())
                    data.append(number)
                except ValueError:
                    print(f"Información incorrecta en {file_path}: {line.strip()}")
            return data
    except FileNotFoundError:
        print(f"No se encontro el archivo: {file_path}")
        return None

def main():
    """Programa 1"""

    mean = [0]
    median = [0]
    mode = [0]
    standard_deviation = [0]
    variance = [0]
    cuenta = [0]

    file_path = input("Ingrese el nombre del archivo .txt: ")

    for n in range(1):
        data = process_file(file_path)

        start_time = time.time()  # Registra el tiempo de inicio

        if data:
            print(n + 1)
            cuenta[n] = len(data)
            mean[n] = calculate_mean(data)
            median[n] = calculate_median(data)
            mode[n] = calculate_mode(data)
            standard_deviation[n] = calculate_standard_deviation(data, mean[n])
            variance[n] = calculate_variance(data, mean[n])

            end_time = time.time()  # Registra el tiempo de finalización
            elapsed_time = end_time - start_time  # Calcula el tiempo transcurrido

            results = f"COUNT: {cuenta[n]}\nMEAN: {mean[n]}\nMEDIAN: {median[n]}\n" \
                      f"MODE: {mode[n]}\nSD: {standard_deviation[n]}\nVARIANCE: {variance[n]}\n" \
                      f"Tiempo transcurrido: {elapsed_time} segundos\n"

            print(results)

            with open("StatisticsResults.txt", 'w', encoding='utf-8') as results_file:
                results_file.write(results)

main()
