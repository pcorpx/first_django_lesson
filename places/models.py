from django.db import models
from tinymce import models as tinymce_models


class Place(models.Model):
    title = models.CharField(max_length=200)
    placeId = models.CharField(max_length=200, blank=True)
    description_short = models.TextField()
    description_long = tinymce_models.HTMLField()
    lat = models.FloatField()
    lng = models.FloatField()

    def __str__(self):
        return f'{self.title}'


class Image(models.Model):
    image = models.ImageField(upload_to='images')
    position = models.IntegerField(default=0, blank=False, null=False)
    place = models.ForeignKey(Place, on_delete=models.CASCADE,
                              related_name='images')

    class Meta:
        ordering = ['position']

    def __str__(self):
        return f'{self.position} {self.place.title}'
