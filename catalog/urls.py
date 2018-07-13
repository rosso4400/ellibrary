from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    #<a href="{% url 'index' %}">Home</a>.
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('book/<int:pk>/update/', views.BookUpdate.as_view(), name='book_update'),
    path('books/create/', views.BookCreate.as_view(), name='book_create'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name = 'author-detail')
]
urlpatterns += [  
    path('authors/create/', views.AuthorCreate.as_view(), name='author_create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author_update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author_delete'),
    path('book/<int:pk>/delete/', views.BookDelete.as_view(), name='book_delete'),
]
