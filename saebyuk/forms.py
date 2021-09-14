from django import forms
from django.db import models
from django.db.models import fields
from django.forms.fields import BooleanField
from saebyuk.models import Book


class RentalForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['thief', 'rental_date', 'return_date', 'available']
        labels = {
            'thief' : '대출자',
            'rental_date' : '대출일',
            'return_date' : '반납예정일',
            'available' : '대출 가능',
        }


class ReturnForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['thief', 'rental_date', 'return_date', 'available']
        labels = {
            'thief' : '대출자',
            'rental_date' : '대출일',
            'return_date' : '반납예정일',
            'available' : '대출 가능',
        }