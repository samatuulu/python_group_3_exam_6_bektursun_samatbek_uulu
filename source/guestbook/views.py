from django.shortcuts import render, redirect, get_object_or_404

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


def book_update(request, pk, *args, **kwargs):
    book = get_object_or_404(GuestBook, pk=pk)
    if request.method == 'GET':
        form = BookForm(data={
            'name': book.name,
            'email': book.email,
            'text': book.text
        })
        return render(request, 'book_update.html', context={'book': book, 'form': form})
    elif request.method == 'POST':
        form = BookForm(data=request.POST)
        if form.is_valid():
            book.name = form.cleaned_data['name']
            book.email = form.cleaned_data['email']
            book.text = form.cleaned_data['text']
            book.save()

            return redirect('home')


def book_delete(request, pk):
    book = get_object_or_404(GuestBook, pk=pk)
    if request.method == 'GET':
        return render(request, 'book_delete.html', context={'book': book})
    elif request.method == 'POST':
        book.delete()
        return redirect('home')