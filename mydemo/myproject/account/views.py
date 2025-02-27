# account/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, UserProfile
from django.contrib import messages

# Create a new book
def create_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        genre = request.POST['genre']
        description = request.POST['description']
        rating = request.POST['rating']
        
        Book.objects.create(title=title, author=author, genre=genre, description=description, rating=rating)
        messages.success(request, 'Book added successfully!')
        return redirect('book_list')

    return render(request, 'books/create_book.html')

# List all books
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

# Edit an existing book
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    
    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.genre = request.POST['genre']
        book.description = request.POST['description']
        book.rating = request.POST['rating']
        book.save()
        messages.success(request, 'Book updated successfully!')
        return redirect('book_list')

    return render(request, 'books/edit_book.html', {'book': book})

# Delete a book
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    messages.success(request, 'Book deleted successfully!')
    return redirect('book_list')

# Recommend books based on ratings
def recommend_books(request):
    books = Book.objects.order_by('-rating')[:5]  # Top 5 rated books
    return render(request, 'books/recommendations.html', {'books': books})
