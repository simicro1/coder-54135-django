from django.urls import path

app_name = "cliente"

from . import views

urlpatterns = [
    # path("home/", views.home),
    path("", views.home, name="home"),
]
