# Generated by Django 3.2.10 on 2021-12-28 10:13

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('places', '0004_place_placeid'),
    ]
    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['position']},
        ),
    ]
