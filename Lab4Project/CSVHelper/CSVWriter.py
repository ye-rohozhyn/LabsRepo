import csv
from typing import List


def write_csv(filename: str, header: List[str], data: List[List[str]]):
    try:
        with open(filename, "w", newline="", encoding="utf-8") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(header)
            csv_writer.writerows(data)
        print(f"Таблиця у форматі CSV створена та збережена у файлі: {filename}")
    except Exception as e:
        print(f"Виникла помилка під час створення файлу CSV: {str(e)}")
