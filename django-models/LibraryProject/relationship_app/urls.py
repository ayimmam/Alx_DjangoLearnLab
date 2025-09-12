from .views import list_books, LibraryDetailView, register, UserLoginView, UserLogoutView
from django.urls import path
from . import views

urlpatterns = [
   path('books/', list_books, name='list_books'),
   path('library/', LibraryDetailView.as_view(), name='library_detail'),
     path('register/', views.register, name='register'),
    path('login/', UserLoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', UserLogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

]