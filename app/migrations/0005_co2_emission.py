# Generated by Django 5.0.4 on 2024-12-26 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_economic_forecast'),
    ]

    operations = [
        migrations.CreateModel(
            name='co2_emission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=100)),
                ('scenario', models.CharField(max_length=100)),
                ('region_category', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=100)),
                ('variable', models.CharField(max_length=100)),
                ('unit', models.CharField(max_length=100)),
                ('year_2020', models.FloatField()),
                ('year_2025', models.FloatField()),
                ('year_2030', models.FloatField()),
                ('year_2035', models.FloatField()),
                ('year_2040', models.FloatField()),
                ('year_2045', models.FloatField()),
                ('year_2050', models.FloatField()),
                ('year_2055', models.FloatField()),
                ('year_2060', models.FloatField()),
                ('year_2065', models.FloatField()),
                ('year_2070', models.FloatField()),
                ('year_2075', models.FloatField()),
                ('year_2080', models.FloatField()),
                ('year_2085', models.FloatField()),
                ('year_2090', models.FloatField()),
                ('year_2095', models.FloatField()),
                ('year_2100', models.FloatField()),
            ],
        ),
    ]
