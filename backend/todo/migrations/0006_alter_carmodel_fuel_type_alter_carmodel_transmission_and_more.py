# Generated by Django 4.2.6 on 2023-11-21 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_car_listing_makes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='fuel_type',
            field=models.CharField(default='Gasoline', max_length=20),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='transmission',
            field=models.CharField(default='Automatics', max_length=15),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='year',
            field=models.IntegerField(default=2023),
        ),
    ]
