from django.urls import path

from hackathon_app import views
urlpatterns = [
    path("", views.home, name = "home"),
]