# Generated by Django 3.2.7 on 2021-09-09 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ufcfrontend', '0002_rename_division_fighter_currentdivision'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fighter',
            name='weight',
        ),
    ]
