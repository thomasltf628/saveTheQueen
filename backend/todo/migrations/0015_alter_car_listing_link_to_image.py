# Generated by Django 4.2.6 on 2023-12-02 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0014_alter_car_listing_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car_listing',
            name='Link_to_image',
            field=models.URLField(blank=True, db_index=True, max_length=256, unique=True, verbose_name='Link'),
        ),
    ]