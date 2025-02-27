# account/models.py
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    description = models.TextField()
    rating = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    favorite_books = models.ManyToManyField(Book, related_name='favorited_by')

    def __str__(self):
        return self.username
