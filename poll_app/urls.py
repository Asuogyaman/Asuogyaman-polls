from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("parliamentary", views.parliamentary, name="parliamentary"),
    path('logout', views.logout, name ="logout"),
]
