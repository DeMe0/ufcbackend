# Generated by Django 3.2.7 on 2021-09-09 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ufcfrontend', '0003_remove_fighter_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='fighter',
            name='img',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
