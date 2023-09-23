from datetime import datetime
from CSVHelper.CSVWriter import *
from CSVHelper.CSVReader import *
from Excel.ExcelWriter import *


def main():
    header, data = read_csv("Employees.csv")
    write_excel("Employees.xlsx", data, header, "all")

    new_header = ["№", "Прізвище", "Ім’я", "По батькові", "Дата народження", "Вік"]
    new_data = []
    for row in data:
        new_row = row[:3] + [row[4]] + [calculate_age(datetime.strptime(row[4], "%d.%m.%Y"))]
        new_data.append(new_row)

    filtered_data_younger_18 = [row for row in new_data if row[4] < 18]
    data_younger_18 = add_index(filtered_data_younger_18)
    add_sheet("Employees.xlsx", data_younger_18, new_header, "younger_18")

    filtered_data_18_45 = [row for row in new_data if 18 <= row[4] <= 45]
    data_18_45 = add_index(filtered_data_18_45)
    add_sheet("Employees.xlsx", data_18_45, new_header, "18-45")

    filtered_data_45_70 = [row for row in new_data if 45 < row[4] <= 70]
    data_45_70 = add_index(filtered_data_45_70)
    add_sheet("Employees.xlsx", data_45_70, new_header, "45-70")

    filtered_data_older_70 = [row for row in new_data if row[4] > 70]
    data_older_70 = add_index(filtered_data_older_70)
    add_sheet("Employees.xlsx", data_older_70, new_header, "older_70")


def calculate_age(birthdate):
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age


def add_index(data: List[List[str]]):
    new_data = []
    index = 1
    for row in data:
        new_row = [index] + row[:5]
        new_data.append(new_row)
        index += 1
    return new_data


main()
