from django.shortcuts import render
from .models import Client, Car, Repair


def project_info(request):
    client = Client.objects.all()
    car = Car.objects.all()
    repair = Repair.objects.all()

    return render(request, 'Lab8App/project_info.html', {'client': client, 'car': car, 'repair': repair})
