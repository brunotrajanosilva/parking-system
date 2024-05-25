from django.urls import path
from . import views

urlpatterns = [
    path("<slug:area>/", views.index, name="index"),
    path("<slug:area>/entry", views.entry, name="entry"),
    path("<slug:area>/exit", views.exit, name="exit"),

    # path('entry', views.entry),
    # path('exit', views.exit)
]
