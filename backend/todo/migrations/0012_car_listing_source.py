# Generated by Django 4.2.6 on 2023-12-02 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0011_car_listing_link_to_image_car_listing_make'),
    ]

    operations = [
        migrations.AddField(
            model_name='car_listing',
            name='source',
            field=models.CharField(default='Unknown', max_length=50),
        ),
    ]
