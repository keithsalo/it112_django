from django.urls import path
from . import views

urlpatterns = [
    path("", views.hello_there, name="home"),
    # path("<username>/", views.hello_there, name="hello_there"),
    path("cars/", views.car2, name="car"),
    path("cars/detail/<str:brand>/", views.car_detail, name="car_detail"),
]
