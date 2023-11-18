import os
import django
import random
from datetime import datetime, timedelta
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Lab8DjangoProject.settings')
django.setup()

from Lab8App.models import Client, Car, Repair

def random_date(start_date, end_date):
    time_between_dates = end_date - start_date
    random_number_of_days = random.randrange(time_between_dates.days)
    return start_date + timedelta(days=random_number_of_days)

clients_data = [
    {
        "ClientCompany": "Company A",
        "CheckingAccount": "ACC123",
        "PhoneNumber": "123456789",
        "ContactPerson": "John Doe",
        "Address": "123 Street, City"
    },
    {
        "ClientCompany": "Company B",
        "CheckingAccount": "ACC456",
        "PhoneNumber": "987654321",
        "ContactPerson": "Jane Smith",
        "Address": "456 Avenue, Town"
    },
]

for client_info in clients_data:
    Client.objects.create(**client_info)

clients = Client.objects.all()

cars_data = [
    {
        "CarBrand": "Brand X",
        "CarPrice": 25000.00,
        "Client": random.choice(clients)
    },
    {
        "CarBrand": "Brand Y",
        "CarPrice": 30000.00,
        "Client": random.choice(clients)
    },
]

for car_info in cars_data:
    Car.objects.create(**car_info)

cars = Car.objects.all()

repairs_data = [
    {
        "StartDate": random_date(timezone.now() - timedelta(days=365), timezone.now()),
        "Car": random.choice(cars),
        "RepairType": "Engine repair",
        "OneHourPrice": 50.00,
        "Discount": 10.00,
        "Hours": 5.0
    },
    {
        "StartDate": random_date(timezone.now() - timedelta(days=365), timezone.now()),
        "Car": random.choice(cars),
        "RepairType": "Brake service",
        "OneHourPrice": 40.00,
        "Discount": 5.00,
        "Hours": 3.5
    },
]

for repair_info in repairs_data:
    Repair.objects.create(**repair_info)
