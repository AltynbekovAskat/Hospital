# Generated by Django 5.1.4 on 2025-01-03 10:08

import multiselectfield.db.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctors',
            name='experience_years_en',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='doctors',
            name='experience_years_ru',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='doctors',
            name='qualifications_en',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='doctors',
            name='qualifications_ru',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='working_days',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('monday', 'monday'), ('tuesday', 'tuesday'), ('wednesday', 'wednesday'), ('thursday', 'thursday'), ('friday', 'friday'), ('saturday', 'saturday'), ('sunday', 'sunday')], max_length=32),
        ),
    ]