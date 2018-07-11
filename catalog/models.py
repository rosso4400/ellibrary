from django.db import models
from django.urls import reverse



class Author(models.Model):
    author_name = models.CharField(max_length=200)

    def __str__(self):
        return self.author_name


class Book(models.Model):
    book_title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author)

    def get_absolute_url(self):
        #return "/catalog/book/%i/" % self.id
        return reverse('book-detail', args=[str(self.id)])

    def __str__(self):
        return self.book_title

