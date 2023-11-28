import csv
import sys
from pathlib import Path
from django.core.management.base import BaseCommand
from todo.models import CarModel

class Command(BaseCommand):
    help = 'Import data from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='C:\\Users\\super\\Capstone_project\\backend\\todo\\Scrapping\\car_data_simple')

    def handle(self, *args, **options):
        csv_file = options['csv_file']

        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                CarModel.objects.create(**row)

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))