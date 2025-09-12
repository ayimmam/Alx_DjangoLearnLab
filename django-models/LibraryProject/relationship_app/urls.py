from . import views
from django.urls import path


urlpatterns = [
   path('books/', views.list_books, name='list_books'),
   path('library/', views.LibraryDetailView.as_view(), name='library_detail'),
   path('register/', views.register, name='register'),
   path('login/', views.UserLoginView.as_view(), name='login'),
   path('logout/', views.UserLogoutView.as_view(), name='logout'),

]