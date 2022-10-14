from django.urls import path
from . import views

urlpatterns = [
    path("karealici/<id>", views.index),
    path("index/<id>", views.index),
    path("theapp01", views.someapp01),
    path("listeleyici/<id>", views.someapp01_details)

]
