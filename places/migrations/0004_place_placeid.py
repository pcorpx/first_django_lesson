# Generated by Django 3.2.10 on 2021-12-27 06:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('places', '0003_image_position'),
    ]
    operations = [
        migrations.AddField(
            model_name='place',
            name='placeId',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
