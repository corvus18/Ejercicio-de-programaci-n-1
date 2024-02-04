"""
wordCount.py
"""

import time

def count_words(file_path):
    """Contar palabras"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            word_count = {}
            for line in file:
                words = line.strip().split()
                for word in words:
                    word_count[word] = word_count.get(word, 0) + 1
            return word_count
    except FileNotFoundError:
        print(f"Archivo no encontrado: {file_path}")
        return None

def process_file(file_path):
    """Procesar file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = file.read()
            return data
    except FileNotFoundError:
        print(f"Archivo no encontrado: {file_path}")
        return None

def main():
    """Contar palabras"""
    file_path = input("Ingrese el nombre del archivo .txt: ")
    data = process_file(file_path)

    start_time = time.time()

    data = process_file(file_path)

    if data:
        word_count = count_words(file_path)

        with open("WordCountResults.txt", 'w', encoding='utf-8') as results_file:
            for word, count in word_count.items():
                print(f"{word} : {count}")
                results_file.write(f"{word} : {count}\n")

        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"\nTime elapsed: {elapsed_time} seconds")
        with open("WordCountResults.txt", 'a', encoding='utf-8') as results_file:
            results_file.write(f"\nTime elapsed: {elapsed_time} seconds\n")

main()
