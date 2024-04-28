from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path('entry', views.entry),
    path('exit', views.exit)
]
