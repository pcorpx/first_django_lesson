# Generated by Django 3.2.10 on 2022-04-16 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0014_remove_place_place_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='slug',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
