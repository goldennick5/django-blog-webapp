from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.homepage, name="home"),
    path("posts/", views.posts, name="posts")
]


