from django.shortcuts import render, redirect
from django.urls import re_path, reverse

def surveys(request):
    return render(request, 'surveys/surveys.html')

def new(request):
    return render(request, 'surveys/new.html')
