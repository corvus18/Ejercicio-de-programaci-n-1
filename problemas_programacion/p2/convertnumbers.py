"""
convertNumbers.py
"""

import time

def convert_to_binary_hexadecimal(data):
    """Convertir a hexadecimal"""
    binary_results = [bin(num)[2:] for num in data]
    hexadecimal_results = [hex(num)[2:].upper() for num in data]
    return binary_results, hexadecimal_results

def process_file(file_path):
    """Procesar file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = []
            for line in file:
                try:
                    number = int(line.strip())
                    data.append(number)
                except ValueError:
                    print(f"Datos invalidos en {file_path}: {line.strip()}")
            return data
    except FileNotFoundError:
        print(f"Archivo no encontrado: {file_path}")
        return None

def main():
    """Convertir numeros"""
    file_path = input("Ingrese el nombre del archivo .txt: ")
    data = process_file(file_path)
    start_time = time.time()

    n = 0

    if data:
        binary_results, hexadecimal_results = convert_to_binary_hexadecimal(data)

        with open("ConversionResults.txt", 'w', encoding='utf-8') as results_file:
            for num, binary, hexa in zip(data, binary_results, hexadecimal_results):
                n = n + 1

                print(f"{n}. Num: {num} | Bin: {binary} | Hex: {hexa}\n")
                results_file.write(f"{n}. Num: {num} | Bin: {binary} | Hex: {hexa}\n")

        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"\nTime elapsed: {elapsed_time} seconds")
        with open("ConversionResults.txt", 'a', encoding='utf-8') as results_file:
            results_file.write(f"\nTime elapsed: {elapsed_time} seconds\n")


    main()
