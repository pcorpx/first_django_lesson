# Generated by Django 3.2.10 on 2021-12-24 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('places', '0001_initial'),
    ]
    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                                           primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                (
                    'place', models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='images', to='places.place'
                    )
                ),
            ],
        ),
    ]
