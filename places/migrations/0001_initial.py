# Generated by Django 3.2.10 on 2021-12-24 08:07

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True, primary_key=True, serialize=False,
                    verbose_name='ID'
                    )
                 ),
                ('title', models.CharField(max_length=200)),
                ('description_short', models.TextField()),
                ('description_long', models.TextField(blank=True)),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
            ],
        ),
    ]
