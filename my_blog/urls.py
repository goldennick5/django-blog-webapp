from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.homepage, name="index"),
    path("about/", views.about, name="about"),
]