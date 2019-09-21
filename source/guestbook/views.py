from django.shortcuts import render

from guestbook.models import GuestBook, BOOK_ACTIVE_CHOICE


def home(request):
    book = GuestBook.objects.filter(status=BOOK_ACTIVE_CHOICE).order_by('-created_at')
    return render(request, 'index.html', context={
        'book': book
    })
