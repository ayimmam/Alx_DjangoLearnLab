from django.http import HttpResponse
from django.shortcuts import render
from .models import Book, Author, Library, Librarian


def library_view(request):
   
    books = Book.objects.all()  # Fetch all book instances from the database
    authors = Author.objects.all()  # Fetch all author instances from the database
    context = {'book_list': books, 'author_list': authors}  # Create a context dictionary with book and author lists
    return render(request, 'books/book_list.html', context)