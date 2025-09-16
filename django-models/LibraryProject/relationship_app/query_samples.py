from relationship_app.models import Author, Book, Library, Librarian

library_name = 'Central Library'
author_name = 'J.K. Rowling'
Book_title = 'Harry Potter and the Sorcerer\'s Stone'
Librarian_name = 'Jane Doe'
# Sample Data 
author1, created = Author.objects.get_or_create(name=author_name)
book1, created = Book.objects.get_or_create(title=Book_title, author=author1)
book2, created = Book.objects.get_or_create(title=Book_title, author=author1)

author2, created = Author.objects.get_or_create(name="George Orwell")
book3, created = Book.objects.get_or_create(title="1984", author=author2)

library1, created = Library.objects.get_or_create(name=library_name)
library1.books.add(book1, book3)

librarian1, created = Librarian.objects.get_or_create(name=Librarian_name, library=library1)
print("--- Query 1: All books by a specific author ---")
authors = Author.objects.get(name=author_name)
for author in authors:
    for book in Book.objects.filter(author=author):
        print(book.title)
print("-" * 20)

for book in Library.objects.get(name="J.K. Rowling").books.all():
    print(book.title)
print("-" * 20)

print("--- Query 2: All books in a library ---")
# Use the Many-to-Many relationship
for book in Library.objects.get(name=library_name).books.all():
    print(book.title)
print("-" * 20)

print("--- Query 3: The librarian for a specific library ---")
# Use the reverse One-to-One relationship
librarian_name = Library.objects.get(name=library_name).books.all()
print(f"The librarian is {librarian_name}")
print("-" * 20)