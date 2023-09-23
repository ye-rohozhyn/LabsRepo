from datetime import datetime
from typing import List
import matplotlib
from CSVHelper.CSVReader import *
import matplotlib.pyplot as plt


def main():
    header, data = read_csv("Employees.csv")
    show_count_males_and_females(data, "Кількість чоловіків та жінок")
    filtered_data_younger_18 = [row for row in data if calculate_age(datetime.strptime(row[4], "%d.%m.%Y")) < 18]
    count_younger_18 = len(filtered_data_younger_18)
    show_count_males_and_females(filtered_data_younger_18, "Кількість чоловіків та жінок молодших за 18")

    filtered_data_18_45 = [row for row in data if 18 <= calculate_age(datetime.strptime(row[4], "%d.%m.%Y")) <= 45]
    show_count_males_and_females(filtered_data_18_45, "Кількість чоловіків та жінок віком від 18 до 45")
    count_18_45 = len(filtered_data_18_45)

    filtered_data_45_70 = [row for row in data if 45 <= calculate_age(datetime.strptime(row[4], "%d.%m.%Y")) <= 70]
    show_count_males_and_females(filtered_data_45_70, "Кількість чоловіків та жінок віком від 45 до 70")
    count_45_70 = len(filtered_data_45_70)

    filtered_data_older_70 = [row for row in data if calculate_age(datetime.strptime(row[4], "%d.%m.%Y")) > 70]
    show_count_males_and_females(filtered_data_older_70, "Кількість чоловіків та жінок старших за 70")
    count_older_70 = len(filtered_data_older_70)

    labels = ["<18", "18-45", "45-70", ">70"]
    counts = [count_younger_18, count_18_45, count_45_70, count_older_70]

    colormap = matplotlib.colormaps["PuBu"]
    norm_counts = [count / max(counts) for count in counts]

    plt.bar(labels, counts, color=[colormap(norm) for norm in norm_counts])

    plt.xlabel("Вікова категорія")
    plt.ylabel("Кількість")
    plt.title("Кількість людей у різних вікових категоріях")

    plt.show()


def calculate_age(birthdate):
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age


def show_count_males_and_females(data: List[List[str]], title: str):
    count_males = 0
    count_females = 0
    for row in data:
        if row[3] == "Чоловік":
            count_males += 1
        else:
            count_females += 1

    print(f"Чоловіків загалом: {count_males}\nЖінок загалом: {count_females}")

    labels = ["Чоловіків", "Жінок"]
    counts = [count_males, count_females]

    plt.bar(labels, counts, color=['lightblue', 'pink'])

    plt.xlabel("Стать")
    plt.ylabel("Кількість")
    plt.title(title)

    plt.show()


main()
