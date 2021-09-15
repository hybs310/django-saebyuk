import datetime

from django import forms
from django.core.checks import messages
from django.db.models.expressions import F
from saebyuk.forms import ReturnForm
from django.db.models import fields
from django.shortcuts import redirect, render, get_object_or_404, redirect
from .models import Book
from .forms import RentalForm, ReturnForm

########################################################################

def index(request):
    #show questions
    book_list = Book.objects.order_by('title')
    context = {'book_list': book_list}
    return render(request, 'saebyuk/book_list.html', context)

########################################################################

def detail(request, book_id):

    book = get_object_or_404(Book, pk=book_id)

    if request.method == "POST":
        form = RentalForm(request.POST, instance=book)
        if form.is_valid():
            rent = form.save(commit=False)
            today = datetime.date.today()
            oneweek = today + datetime.timedelta(days=7)
            rent.rental_date = today
            rent.return_date = oneweek
            rent.thief = request.user
            rent.available = False
            rent.save()
            return redirect('saebyuk:detail', book_id=book.id)
    context = {'book': book}
    return render(request, 'saebyuk/book_detail.html', context)

########################################################################

def book_return(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    form = ReturnForm(request.POST, instance=book)
    rtn = form.save(commit=False)
    if(rtn.thief == request.user):
        rtn.rental_date = None
        rtn.return_date = None
        rtn.thief = None
        rtn.available = True
        rtn.save()
        return redirect('saebyuk:detail', book_id=book.id)
    else:
        return redirect('saebyuk:detail', book_id=book.id)

