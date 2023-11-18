# Generated by Django 4.2.7 on 2023-11-18 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CarBrand', models.CharField(max_length=255)),
                ('CarPrice', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ClientCompany', models.CharField(max_length=255)),
                ('CheckingAccount', models.CharField(max_length=255)),
                ('PhoneNumber', models.CharField(max_length=15)),
                ('ContactPerson', models.CharField(max_length=255)),
                ('Address', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Repair',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StartDate', models.DateField()),
                ('RepairType', models.CharField(max_length=255)),
                ('OneHourPrice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Discount', models.DecimalField(decimal_places=2, max_digits=4)),
                ('Hours', models.DecimalField(decimal_places=2, max_digits=6)),
                ('Car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Lab8App.car')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='Client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Lab8App.client'),
        ),
    ]
