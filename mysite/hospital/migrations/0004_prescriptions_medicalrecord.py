# Generated by Django 5.1.4 on 2025-01-05 09:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0003_appointments_notes_en_appointments_notes_ru_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescriptions',
            name='medicalRecord',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hospital.medicalrecord'),
            preserve_default=False,
        ),
    ]
