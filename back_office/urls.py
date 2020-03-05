from django.urls import path
from back_office import views

urlpatterns = [
    path("", views.home, name="home"),
    path("test/", views.test, name="test")
]