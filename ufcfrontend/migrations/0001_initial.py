# Generated by Django 3.2.7 on 2021-09-09 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fighter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('nickname', models.CharField(max_length=100)),
                ('division', models.CharField(max_length=100)),
                ('weight', models.CharField(max_length=100)),
                ('record', models.CharField(max_length=100)),
            ],
        ),
    ]
