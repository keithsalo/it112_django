from django.urls import path
from homework_6 import views

urlpatterns = [
    path("", views.home, name="home"),
    path("<username>/", views.hello_there, name="hello_there"),
]
