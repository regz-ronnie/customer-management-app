# books/urls.py
from django.urls import path
from .views import create_book, book_list, edit_book, delete_book, recommend_books

urlpatterns = [
    path('books/', book_list, name='book_list'),
    path('books/create/', create_book, name='create_book'),
    path('books/edit/<int:book_id>/', edit_book, name='edit_book'),
    path('books/delete/<int:book_id>/', delete_book, name='delete_book'),
    path('books/recommend/', recommend_books, name='recommend_books'),
]
