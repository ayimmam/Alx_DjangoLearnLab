from django.db import models

class Author(models.Model):
    author_full_name = models.CharField(max_length=200)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

class Library(models.Model):
    book_titles = models.CharField(max_length=200)
    books = models.ManyToManyField(Book, related_name='libraries') # M:M

class Librarian(models.Model):
    name = models.CharField(max_length=200)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarian') # 1:1
