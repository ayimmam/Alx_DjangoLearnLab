from django.http import HttpResponse
from django.shortcuts import render
from .models import Book, Author 
from .models import Library
from django.views.generic.detail import DetailView
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView

def list_books(request):
   
    books = Book.objects.all()  # Fetch all book instances from the database
    authors = Author.objects.all()  # Fetch all author instances from the database
    context = {'book_list': books, 'author_list': authors}  # Create a context dictionary with book and author lists
    return render(request, 'relationship_app/list_books.html', context)
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    
# Custom registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('book_list')  # Redirect to a home page or book list after registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Use Django's built-in views for login and logout
class UserLoginView(LoginView):
    template_name = 'relationship_app/login.html'

class UserLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'