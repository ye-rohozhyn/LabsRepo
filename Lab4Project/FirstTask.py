import random
from datetime import timedelta, date
from faker import Faker
from CSVHelper.CSVWriter import *


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


def main():
    header = ["Прізвище", "Ім’я", "По батькові", "Стать", "Дата народження", "Посада", "Місто проживання", "Адреса проживання", "Телефон", "Email"]
    data = generate_data(2000)
    write_csv("Employees.csv", header, data)


fake = Faker('uk_UA')
main()
