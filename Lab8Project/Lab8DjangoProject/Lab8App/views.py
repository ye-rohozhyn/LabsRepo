from django.shortcuts import render
from .models import Client, Car, Repair


def project_info(request):
    errors = Client.objects.all()
    programmers = Car.objects.all()
    error_corrections = Repair.objects.all()

    return render(request, 'software_company_app/project_info.html', {'errors': errors, 'programmers': programmers, 'corrections': error_corrections})
