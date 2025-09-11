from bookshelf.models import Book
book_1984 = Book.objects.create(title='1984', author='George Orwell', publication_year=1949)

Expected Output:
The command will return the newly created Book instance.

>>> book_1984
<Book: Book object (1)>