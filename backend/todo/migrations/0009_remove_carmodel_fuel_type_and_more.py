# Generated by Django 4.2.6 on 2023-11-28 01:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0008_remove_profile_bio_remove_profile_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carmodel',
            name='fuel_type',
        ),
        migrations.RemoveField(
            model_name='carmodel',
            name='transmission',
        ),
        migrations.RemoveField(
            model_name='carmodel',
            name='year',
        ),
    ]
