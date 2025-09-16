from relationship_app.models import Author, Book, Library, Librarian

library_name = 'Central Library'
author_name = 'J.K. Rowling'
book_title = 'Harry Potter and the Sorcerer\'s Stone'
Librarian_name = 'Jane Doe'

# Sample Data 
author1, created = Author.objects.get_or_create(full_name=author_name)
book1, created = Book.objects.get_or_create(title=book_title, author=author1)
book2, created = Book.objects.get_or_create(title='Harry Potter and the Chamber of Secrets', author=author1)

author2, created = Author.objects.get_or_create(full_name="George Orwell")
book3, created = Book.objects.get_or_create(title="1984", author=author2)

library1, created = Library.objects.get_or_create(library_books_title=library_name)
library1.books.add(book1, book3)

librarian1, created = Librarian.objects.get_or_create(library=library1, name=Librarian_name)

print("--- Query 1: All books by a specific author ---")
author_obj = Author.objects.get(full_name=author_name)
for book in author_obj.books.all():
    print(book.title)
print("-" * 20)

print("--- Query 2: All books in a library ---")
# Use the Many-to-Many relationship
for book in Library.objects.get(library_books_title=library_name).books.all():
    print(book.title)
print("-" * 20)

print("--- Query 3: The librarian for a specific library ---")
# Use the reverse One-to-One relationship
library_obj = Library.objects.get(library_books_title=library_name)
print(f"The librarian is {library_obj.librarian.name}")
print("-" * 20)