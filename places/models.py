from tkinter.tix import Tree
from django.db import models
from tinymce import models as tinymce_models


class Place(models.Model):
    title = models.CharField(max_length=200, unique=True,
                             verbose_name='Название')
    slug = models.CharField(max_length=200, unique=True,
                            verbose_name='Метка')
    description_short = models.TextField(
        verbose_name='Короткое описание',
        blank=True
    )
    description_long = tinymce_models.HTMLField(
        verbose_name='Полное описание',
        blank=True,
    )
    lat = models.FloatField(verbose_name='Широта')
    lng = models.FloatField(verbose_name='Долгота')

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(upload_to='images', verbose_name='Изображение')
    position = models.IntegerField(default=0, blank=False, null=False,
                                   verbose_name='Позиция')
    place = models.ForeignKey(Place, on_delete=models.CASCADE,
                              related_name='images', verbose_name='Место')

    class Meta:
        ordering = ['position']

    def __str__(self):
        return f'{self.position} {self.place.title}'
