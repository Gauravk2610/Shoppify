from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.delivery , name="Delivery"),
    path('<int:id>', views.delivery_details , name="Delivery Details"),
]