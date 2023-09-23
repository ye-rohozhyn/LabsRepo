import csv


def read_csv(filename: str):
    try:
        with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
            csvreader = csv.reader(csvfile)
            header = next(csvreader)
            data = [row for row in csvreader]

        print("Файл успішно зчитано")
        return header, data
    except Exception as e:
        print(f"Виникла помилка під час зчитування файлу CSV: {str(e)}")
