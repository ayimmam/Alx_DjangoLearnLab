from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import user_passes_test, permission_required
from django.forms import ModelForm
from .models import Book, UserProfile, Library, Author, CustomUser

# Forms
class BookForm(ModelForm):
    """A form for the Book model."""
    class Meta:
        model = Book
        fields = ['title', 'author']

# --- Unmodified Code (kept together) ---

# Existing views (included for completeness)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/book_list.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
def register(request):
    """View to handle user registration."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('member_view')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

class UserLoginView(LoginView):
    """A class-based view for user login."""
    template_name = 'relationship_app/login.html'

class UserLogoutView(LogoutView):
    """A class-based view for user logout."""
    template_name = 'relationship_app/logout.html'

# Helper functions for the @user_passes_test decorator
def is_admin(user):
    """Checks if the user has the 'Admin' role."""
    return user.is_authenticated and hasattr(user, 'profile') and user.profile.role == 'Admin'

def is_librarian(user):
    """Checks if the user has the 'Librarian' role."""
    return user.is_authenticated and hasattr(user, 'profile') and user.profile.role == 'Librarian'

def is_member(user):
    """Checks if the user has the 'Member' role."""
    return user.is_authenticated and hasattr(user, 'profile') and user.profile.role == 'Member'

# Role-specific views with decorators
@user_passes_test(is_admin)
def admin_view(request):
    """View only accessible to Admin users."""
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    """View only accessible to Librarian users."""
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    """View only accessible to Member users."""
    return render(request, 'relationship_app/member_view.html')

# Views with custom permission checks
@permission_required('relationship_app.can_add_book')
def add_book(request):
    """View to add a new book, requires 'can_add_book' permission."""
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form})

@permission_required('relationship_app.can_change_book')
def change_book(request, pk):
    """View to change an existing book, requires 'can_change_book' permission."""
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/change_book.html', {'form': form})

@permission_required('relationship_app.can_delete_book')
def delete_book(request, pk):
    """View to delete a book, requires 'can_delete_book' permission."""
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'relationship_app/delete_book.html', {'book': book})
