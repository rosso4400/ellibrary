from django.db import models
from django.urls import reverse


class Author(models.Model):
    author_name = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    #def save(self, *args, **kwargs):
        #if Author.objects.get(author_name="Lev Tolstoy"): 
            #return # You cannot add this author because someone else has beat you to it 
        #else:
            #super(Author, self).save(*args, **kwargs)

    def __str__(self):
        return self.author_name


class Book(models.Model):
    book_title = models.CharField(max_length=200)
    author = models.ManyToManyField(Author)

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

    def display_author(self):
        return ', '.join([ author.author_name for author in self.author.all() ])
    display_author.short_description = 'Author'
        
    def __str__(self):
        return self.book_title

