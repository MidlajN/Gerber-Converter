from django.urls import path
from GerberApp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload', views.upload_gerber, name='upload'),
]