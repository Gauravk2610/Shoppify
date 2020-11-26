from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="Login"),
    path('signup', views.signup, name="Signup"),
    path('login', views.loginhandle, name="Loginhandle"),
    path('logout', views.logouthandle, name="Logouthandle"),

]