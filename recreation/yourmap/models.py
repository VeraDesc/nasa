from __future__ import unicode_literals

from django.db import models

# Create your models here.

class GeoTag(models.Model):
    title = models.CharField(max_length=512)
    lat = models.DecimalField(max_digits=12,decimal_places=9)
    lng = models.DecimalField(max_digits=12,decimal_places=9)
    alt = models.DecimalField(max_digits=12,decimal_places=7,default=0.0)

class MediaType(models.Model):
    code = models.CharField(max_length=24)

class Media(models.Model):
    type = models.ForeignKey(MediaType, on_delete=models.CASCADE)
    ref = models.TextField()
