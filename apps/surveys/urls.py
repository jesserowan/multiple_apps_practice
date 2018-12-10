from django.urls import path
from . import views


app_name = 'surveys'
urlpatterns = [
    path('', views.surveys, name="surveys"),
    path('new', views.new, name="new")
]