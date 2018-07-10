from django.shortcuts import render
from django.views import generic

from .models import Book, Author


def index(request):
    return render(
        request,
        'index.html',
    )


class BookListView(generic.ListView):
    model = Book


class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author
