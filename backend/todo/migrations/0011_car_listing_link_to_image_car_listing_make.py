# Generated by Django 4.2.6 on 2023-12-02 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0010_car_listing_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='car_listing',
            name='link_to_image',
            field=models.URLField(blank=True, db_index=True, default=None, max_length=256, unique=True, verbose_name='Link'),
        ),
        migrations.AddField(
            model_name='car_listing',
            name='make',
            field=models.CharField(default='Unknown', max_length=50),
        ),
    ]
