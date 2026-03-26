from django.urls import path

from hackathon_app import views
urlpatterns = [
    path("", views.home, name = "home"),
    path("catalogue/", views.catalogue, name = "catalogue"),
    path("register/",views.register_view ,name = "register"),
    path("login/",views.login_page, name = "login"),
    path("logout/",views.logout_page, name = "logout"),
]