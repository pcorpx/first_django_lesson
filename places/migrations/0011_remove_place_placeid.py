# Generated by Django 3.2.10 on 2022-04-16 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0010_auto_20220416_2031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='placeId',
        ),
    ]
