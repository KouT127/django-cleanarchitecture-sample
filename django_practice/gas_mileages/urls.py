from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'gas_mileages'
urlpatterns = [
    path('', views.index, name='index'),
    url(r'^(?P<pk>\d+)/delete/$', views.delete, name='delete'),
]