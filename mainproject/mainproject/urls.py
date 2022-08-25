from django.conf.urls import url
from firstWEB import views


urlpatterns = [
    url(r'^$', views.index),
]
