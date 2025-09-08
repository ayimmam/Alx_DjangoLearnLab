from bookshelf.models import Book
book = Book.objects.get(title='Nineteen Eighty-Four')
book.delete()

# Confirm deletion by trying to retrieve the book again.
try:
    Book.objects.get(title='Nineteen Eighty-Four')
except Book.DoesNotExist:
    print("Book has been successfully deleted.")

Expected Output
The expected output shows the confirmation message, indicating that the DoesNotExist exception was caught, which means the book was successfully removed from the database.

>>> book = Book.objects.get(title='Nineteen Eighty-Four')
>>> book.delete()
(1, {'bookshelf.Book': 1})
>>> try:
...     Book.objects.get(title='Nineteen Eighty-Four')
... except Book.DoesNotExist:
...     print("Book has been successfully deleted.")
... 
Book has been successfully deleted.