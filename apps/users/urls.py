from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
    path('', views.register),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('users/new', views.register),
    path('users', views.users)
]