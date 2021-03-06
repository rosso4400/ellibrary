from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
import operator

from .models import Book, Author


@login_required
def index(request):
    return render(
        request,
        'index.html',
    )


class BookListView(LoginRequiredMixin, generic.ListView):
    model = Book
    def get_queryset(self):
        result = super(BookListView, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            result = result.filter(Q(book_title__icontains=query) | Q(author__author_name__icontains=query))
        return result


class BookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Book


class AuthorListView(LoginRequiredMixin, generic.ListView):
    model = Author
    def get_queryset(self):
        result = super(AuthorListView, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            result = result.filter(Q(author_name__icontains=query))
        return result


class AuthorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Author


class BookUpdate(LoginRequiredMixin, UpdateView):
    model = Book
    fields = ['book_title', 'author']
    #template_name_suffix = '_update'


class BookCreate(LoginRequiredMixin, CreateView):
    model = Book
    fields = ['book_title', 'author']


class BookDelete(LoginRequiredMixin, DeleteView):
    model = Book
    success_url = reverse_lazy('books')


class AuthorCreate(LoginRequiredMixin, CreateView):
    model = Author
    fields = ['author_name']


class AuthorUpdate(LoginRequiredMixin, UpdateView):
    model = Author
    fields = ['author_name']


class AuthorDelete(LoginRequiredMixin, DeleteView):
    model = Author
    success_url = reverse_lazy('authors')

            


