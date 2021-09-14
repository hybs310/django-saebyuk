import datetime
from saebyuk.forms import ReturnForm
from django.db.models import fields
from django.shortcuts import redirect, render, get_object_or_404, redirect
from .models import Book
from .forms import RentalForm

def index(request):
    #show questions
    book_list = Book.objects.order_by('-title')
    context = {'book_list': book_list}
    return render(request, 'saebyuk/book_list.html', context)


def detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    if request.method == "POST":
        form = ReturnForm(request.POST, instance=book)
        if form.is_valid():
            rtn = form.save(commit=False)
            rtn.rental_date = None
            rtn.return_date = None
            rtn.thief = None
            rtn.available = True
            rtn.save()
            return redirect('saebyuk:detail', book_id=book.id)
    context = {'book': book}
    return render(request, 'saebyuk/book_detail.html', context)

def rent(request, book_id):

    book = get_object_or_404(Book, pk=book_id)


    if request.method == "POST":
        form = RentalForm(request.POST, instance=book)
        if form.is_valid():
            rent = form.save(commit=False)
            today = datetime.date.today()
            oneweek = today + datetime.timedelta(days=7)
            rentreq = form.save(commit=False)
            rent.rental_date = today
            rent.return_date = oneweek
            rent.thief = request.user
            rent.available = False
            rent.save()
            return redirect('saebyuk:detail', book_id=book.id)
    else:
        book = get_object_or_404(Book, pk=book_id)
        form = RentalForm
    context = {'book': book, 'form': form}
    return render(request, 'saebyuk/rental_form.html',  context)
