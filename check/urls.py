from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),                            #   панель администартора
    path('', views.main, name="main"),
]