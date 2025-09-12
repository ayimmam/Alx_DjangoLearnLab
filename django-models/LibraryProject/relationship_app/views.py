from django.http import HttpResponse
from django.shortcuts import render
from .models import Book, Author 
from .models import Library
from django.views.generic.detail import DetailView

def library_view(request):
   
    books = Book.objects.all()  # Fetch all book instances from the database
    authors = Author.objects.all()  # Fetch all author instances from the database
    context = {'book_list': books, 'author_list': authors}  # Create a context dictionary with book and author lists
    return render(request, 'relationship_app/list_books.html', context)
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'