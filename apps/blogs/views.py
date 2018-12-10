from django.shortcuts import render, redirect
from django.urls import re_path, reverse


def index(request):
    return render(request, 'blogs/index.html')

def new(request):
    return render(request, 'blogs/new.html')

def create(request):
    return redirect('blogs:blogs')

def show(request, number):
    context = {
        "number": number
    }
    return render(request, 'blogs/show.html', context)

def edit(request, number):
    context = {
        "number": number
    }
    return render(request, 'blogs/edit.html', context)

def delete(request, number):
    return redirect('blogs:blogs')
