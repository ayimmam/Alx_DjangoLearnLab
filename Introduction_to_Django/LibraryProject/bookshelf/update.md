from bookshelf.models import Book
book_to_update = Book.objects.get(title='1984')
book_to_update.title = 'Nineteen Eighty-Four'
book_to_update.save()
print(book_to_update.title)

Expected Output
The expected output shows the updated title of the book instance, confirming that the changes were saved successfully.

>>> book_to_update = Book.objects.get(title='1984')
>>> book_to_update.title = 'Nineteen Eighty-Four'
>>> book_to_update.save()
>>> print(book_to_update.title)
Nineteen Eighty-Four
