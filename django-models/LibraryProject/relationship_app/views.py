from django.http import HttpResponse
from django.shortcuts import render
from .models import Book, Author, Library, Librarian
from django.views.generic import DetailView


def library_view(request):
   
    books = Book.objects.all()  # Fetch all book instances from the database
    authors = Author.objects.all()  # Fetch all author instances from the database
    context = {'book_list': books, 'author_list': authors}  # Create a context dictionary with book and author lists
    return render(request, 'relationship_app/list_books.html', context)
class BookDetailView(DetailView):
  """A class-based view for displaying details of a specific book."""
  model = Book
  template_name = 'relationship_app/library_detail.html'

  def display_book_details(request, book_id,**kwargs):
    """Injects additional context data specific to the book."""
    context = super().get_context_data(**kwargs)
    context['book_id'] = book_id
    return context

  def get_context_data(self, **kwargs):
    """Injects additional context data specific to the book."""
    context = super().get_context_data(**kwargs)
    context['book_id'] = self.kwargs['book_id']
    return context          
    book = self.get_object()  # Retrieve the current book instance
    