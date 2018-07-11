from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView

from .models import Book, Author


@login_required
def index(request):
    return render(
        request,
        'index.html',
    )


class BookListView(LoginRequiredMixin, generic.ListView):
    model = Book


class BookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Book


class AuthorListView(LoginRequiredMixin, generic.ListView):
    model = Author


class BookUpdate(UpdateView):
    model = Book
    fields = ['book_title', 'authors']
    template_name_suffix = '_update'


class BookCreate(CreateView):
    model = Book
    fields = ['book_title', 'authors']


