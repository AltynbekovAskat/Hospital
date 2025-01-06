# Generated by Django 5.1.4 on 2025-01-05 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0005_remove_appointments_patient_id_en_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prescriptions',
            name='patient_id_en',
        ),
        migrations.RemoveField(
            model_name='prescriptions',
            name='patient_id_ru',
        ),
        migrations.RemoveField(
            model_name='prescriptions',
            name='staff_id_en',
        ),
        migrations.RemoveField(
            model_name='prescriptions',
            name='staff_id_ru',
        ),
        migrations.AddField(
            model_name='speciality',
            name='speciality_name_en',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='speciality',
            name='speciality_name_ru',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
