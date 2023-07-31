from django.urls import path

from . import views
app_name = "library"

urlpatterns = [
    path("", views.Front_look, name = "Front_look"),
    path("login_test/work/", views.Work_area, name = "Work_area"),
    ]