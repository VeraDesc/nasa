
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new-geo-tag$', views.add_geotag, name='add_geotag'),
    url(r'^edit-geo-tag$', views.edit_geotag, name='edit_geotag'),
]
