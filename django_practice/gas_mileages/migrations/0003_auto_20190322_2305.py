# Generated by Django 2.1.5 on 2019-03-22 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motorcycles', '0003_auto_20190303_0739'),
        ('gas_mileages', '0002_auto_20190319_1337'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gasmileage',
            name='bike',
        ),
        migrations.AddField(
            model_name='gasmileage',
            name='bike',
            field=models.ManyToManyField(to='motorcycles.Motorcycle'),
        ),
    ]
