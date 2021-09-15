from os import name
from config import settings
from django.urls import path
from . import views

app_name = 'saebyuk'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:book_id>/', views.detail, name='detail'),
    path('return/<int:book_id>/', views.book_return, name='book_return'),
] 