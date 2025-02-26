import csv
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'econsent.settings')
django.setup()
from app.models import energy_cost

def import_data(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            energy_cost.objects.create(
                model_name=row['Model'],
                scenario=row['Scenario'],
                region_category=row['Region_Category'],
                region=row['Region'],
                variable=row['Variable'],
                unit=row['Unit'],
                year_2020=row['2020'] if row['2020'] else 0,
                year_2025=row['2025'] if row['2025'] else 0,
                year_2030=row['2030'] if row['2030'] else 0,
                year_2035=row['2035'] if row['2035'] else 0,
                year_2040=row['2040'] if row['2040'] else 0,
                year_2045=row['2045'] if row['2045'] else 0,
                year_2050=row['2050'] if row['2050'] else 0,
                year_2055=row['2055'] if row['2055'] else 0,
                year_2060=row['2060'] if row['2060'] else 0,
                year_2065=row['2065'] if row['2065'] else 0,
                year_2070=row['2070'] if row['2070'] else 0,
                year_2075=row['2075'] if row['2075'] else 0,
                year_2080=row['2080'] if row['2080'] else 0,
                year_2085=row['2085'] if row['2085'] else 0,
                year_2090=row['2090'] if row['2090'] else 0,
                year_2095=row['2095'] if row['2095'] else 0,
                year_2100=row['2100'] if row['2100'] else 0,
            )

if __name__ == '__main__':
    csv_file_path = 'D:/electronic-consent-master/Data_tables/Energy_cost.csv' 
    import_data(csv_file_path)
    print("Data imported successfully.")
