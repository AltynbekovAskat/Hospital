# Generated by Django 5.1.4 on 2025-01-06 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0008_alter_appointments_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='direction_and_services',
            name='name_en',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='direction_and_services',
            name='name_ru',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='hospital',
            name='address_en',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='hospital',
            name='address_ru',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='hospital',
            name='hospital_name_en',
            field=models.CharField(max_length=32, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='hospital',
            name='hospital_name_ru',
            field=models.CharField(max_length=32, null=True, unique=True),
        ),
    ]
