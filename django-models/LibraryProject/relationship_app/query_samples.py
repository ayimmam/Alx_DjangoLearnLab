from relationship_app.models import Author, Book, Library, Librarian

# Sample Data 
author1, created = Author.objects.get_or_create(name="J.K. Rowling")
book1, created = Book.objects.get_or_create(title="Harry Potter and the Sorcerer's Stone", author=author1)
book2, created = Book.objects.get_or_create(title="Harry Potter and the Chamber of Secrets", author=author1)

author2, created = Author.objects.get_or_create(name="George Orwell")
book3, created = Book.objects.get_or_create(title="1984", author=author2)

library1, created = Library.objects.get_or_create(name="Library_name")
library1.books.add(book1, book3)

librarian1, created = Librarian.objects.get_or_create(name="Jane Doe", library=library1)

print("--- Query 1: All books by a specific author ---")
# Use the reverse relationship from Author to Book
for book in Author.objects.get(name="J.K. Rowling").books.all():
    print(book.title)
print("-" * 20)

print("--- Query 2: All books in a library ---")
# Use the Many-to-Many relationship
for book in Library.objects.get(name="Library_name").books.all():
    print(book.title)
print("-" * 20)

print("--- Query 3: The librarian for a specific library ---")
# Use the reverse One-to-One relationship
librarian_name = Library.objects.get(name="Library_name")
print(f"The librarian is {librarian_name}")
print("-" * 20)