
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class GeoTag(models.Model):
    title = models.CharField(max_length=512)
    lat = models.DecimalField(max_digits=8,decimal_places=4)
    lng = models.DecimalField(max_digits=8,decimal_places=4)
    alt = models.DecimalField(max_digits=8,decimal_places=5,default=0.0)

    def __str__(self):
        return self.title

class MediaType(models.Model):
    code = models.CharField(max_length=24)

    def __str__(self):
        return self.code


class Media(models.Model):
    type = models.ForeignKey(MediaType, on_delete=models.CASCADE)
    ref = models.TextField()
