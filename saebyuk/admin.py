from django.contrib import admin
from django.shortcuts import render
from .models import Book


class BooklistSearch(admin.ModelAdmin):
    search_fields = ['title']



admin.site.register(Book, BooklistSearch)

# Register your models here.
