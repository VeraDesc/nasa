
from django.contrib import admin

from . import models

admin.site.register(models.GeoTag)
admin.site.register(models.MediaType)
admin.site.register(models.Media)
