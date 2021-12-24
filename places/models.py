from django.db import models

# Create your models here.
class Place(models.Model):
    title = models.CharField(max_length=200)
    description_short = models.TextField()
    description_long = models.TextField(blank=True)
    lat = models.FloatField()
    lng = models.FloatField()
    def __str__(self):
        return self.title