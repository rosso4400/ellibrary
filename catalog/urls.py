from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    #<a href="{% url 'index' %}">Home</a>.
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('book/update/<int:pk>/', views.BookUpdate.as_view(), name='book-update'),
    path('books/create/', views.BookCreate.as_view(), name='book-create'),
]
