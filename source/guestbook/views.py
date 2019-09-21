from django.shortcuts import render, redirect

from guestbook.forms import BookForm
from guestbook.models import GuestBook, BOOK_ACTIVE_CHOICE


def home(request):
    book = GuestBook.objects.filter(status=BOOK_ACTIVE_CHOICE).order_by('-created_at')
    return render(request, 'index.html', context={
        'book': book
    })


def book_create(request, *args, **kwargs):
    if request.method == 'GET':
        form = BookForm()
        return render(request, 'book_create.html', context={'form': form})
    elif request.method == 'POST':
        form = BookForm(data=request.POST)
        if form.is_valid():
            GuestBook.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                text=form.cleaned_data['text'],
            )
            response = redirect('home')
            return response
        else:
            return render(request, 'book_create.html', context={'form': form})