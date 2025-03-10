""" urls for home page link"""

from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home')
]
