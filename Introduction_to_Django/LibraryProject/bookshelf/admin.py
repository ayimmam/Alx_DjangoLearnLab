from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    
    list_display = ('title', 'author', 'publication_year')
    
    # Add a list filter sidebar to easily filter books by publication year.
    list_filter = ('publication_year',)
    
    # Enable a search bar to search for books by their title or author.
    search_fields = ('title', 'author')

# Register the Book model with the custom admin class and use this configuration
admin.site.register(Book, BookAdmin)