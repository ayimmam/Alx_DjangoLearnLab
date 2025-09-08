from bookshelf.models import Book
book = Book.objects.get(title='1984')
book.title = 'Nineteen Eighty-Four'
book.save()
print(book.title)

Expected Output
The expected output shows the updated title of the book instance, confirming that the changes were saved successfully.

>>> book = Book.objects.get(title='1984')
>>> book.title = 'Nineteen Eighty-Four'
>>> book.save()
>>> print(book.title)
Nineteen Eighty-Four
