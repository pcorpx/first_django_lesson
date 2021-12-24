from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=200)
    description_short = models.TextField()
    description_long = models.TextField(blank=True)
    lat = models.FloatField()
    lng = models.FloatField()
    def __str__(self):
        return f'{self.title}'


class Image(models.Model):
    image = models.ImageField(upload_to='images')
    position = models.IntegerField()
    place = models.ForeignKey(Place, on_delete=models.CASCADE, 
        related_name='images'
    )
    def __str__(self):
        return f'{self.position} {self.place.title}'