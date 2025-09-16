from .views import book_list, LibraryDetailView, register, UserLoginView, UserLogoutView
from django.urls import path
from . import views

urlpatterns = [
   path('books/', book_list, name='list_books'),
   path('library/', LibraryDetailView.as_view(), name='library_detail'),
  path('register/', views.register, name='register'),
  path('login/', UserLoginView.as_view(template_name='relationship_app/login.html'), name='login'),
  path('logout/', UserLogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    # Role-based views
    path('admin_dashboard/', views.admin_view, name='admin_view'),
    path('librarian_dashboard/', views.librarian_view, name='librarian_view'),
    path('member_dashboard/', views.member_view, name='member_view'),
    path('book/add/', views.add_book, name='add_book'),
    path('book/<int:pk>/change/', views.change_book, name='change_book'),
    path('book/<int:pk>/delete/', views.delete_book, name='delete_book'),
]