from CSVHelper.CSVReader import *
from Excel.ExcelWriter import *
import matplotlib.pyplot as plt


def main():
    header, data = read_csv("Employees.csv")
    write_excel("Employees.xlsx", data, header, "all")

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
    plt.title("Кількість чоловіків та жінок")

    plt.show()


main()
