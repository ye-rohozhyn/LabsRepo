import random
from datetime import datetime, timedelta, date
from faker import Faker
from CSVHelper.CSVWriter import *
from CSVHelper.CSVReader import *
from Excel.ExcelWriter import *


def generate_data(num_records):
    data = []
    for _ in range(num_records):
        gender = random.choice(["Чоловік", "Жінка"])
        birthdate = random_birthdate()
        last_name = fake.last_name_male() if gender == "Чоловік" else fake.last_name_female()
        first_name = fake.first_name_male() if gender == "Чоловік" else fake.first_name_female()
        middle_name = generate_middle_name(gender)
        position = fake.job()
        city = fake.city()
        address = fake.address()
        phone_number = fake.phone_number()
        email = fake.email()

        data.append(
            [last_name, first_name, middle_name, gender, birthdate.strftime("%d.%m.%Y"), position, city, address,
             phone_number, email])

    return data


def random_birthdate():
    start_date = date(1938, 1, 1)
    end_date = date(2008, 12, 31)
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)


def generate_middle_name(gender):
    first_name = fake.first_name_male()
    if gender == "Чоловік":
        if first_name[-1] in ['є', 'й']:
            middle_name = first_name[:-1] + "йович"
        elif first_name[-1] in ['о']:
            middle_name = first_name + "вич"
        else:
            middle_name = first_name + "ович"
    else:
        if first_name[-1] in ['а', 'я', 'й']:
            middle_name = first_name[:-1] + "ївна"
        elif first_name[-1] in ['і']:
            middle_name = first_name + "вна"
        else:
            middle_name = first_name + "івна"

    return middle_name


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


def main():
    header = ["Прізвище", "Ім’я", "По батькові", "Стать", "Дата народження", "Посада", "Місто проживання", "Адреса проживання", "Телефон", "Email"]
    data = generate_data(2000)
    write_csv("Employees.csv", header, data)

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


if __name__ == '__main__':
    fake = Faker('uk_UA')
    main()
