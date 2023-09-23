import csv


def read_csv(filename: str):
    with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        header = next(csvreader)
        data = [row for row in csvreader]

    return header, data
