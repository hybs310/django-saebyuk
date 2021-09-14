from os import name
from config import settings
from django.urls import path
from . import views

app_name = 'saebyuk'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:book_id>/', views.detail, name='detail'),
    path('rent/<int:book_id>/', views.rent, name='rent'),
] 