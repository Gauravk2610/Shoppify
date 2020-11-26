from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="Index"),
    path('<int:id>', views.product, name="product"),
    path('contact/', views.contact, name="contact"),
    path('checkout/', views.checkout, name="checkout"),
    path('tracker/', views.tracker, name="tracker"),
    path('about/', views.about, name="about"),
    path('team/', views.team, name="team"),
    path('subscriber', views.subscriber, name="subscriber"),
    path('thanks/', views.thanks, name="thanks"),
]