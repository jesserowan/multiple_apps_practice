from django.shortcuts import render, redirect
from django.urls import re_path, reverse
from . import views

def register(request):
    return render(request, 'users/register.html')

def login(request):
    return render(request, 'users/login.html')

def users(request):
    return render(request, 'users/users.html')