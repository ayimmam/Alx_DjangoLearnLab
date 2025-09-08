1. Create Operation
Command:
To create a new Book instance, import the model and instantiate it with the desired data, then call the .save() method.

from bookshelf.models import Book
new_book = Book(title='1984', author='George Orwell', publication_year=1949)
new_book.save()

Expected Output:
The save() command does not produce any output on success. A new line indicates that the operation was successful.

>>> 

2. Retrieve Operation
Command:
To retrieve the book instance you just created, use the objects.get() method. You can then print its attributes to confirm the data.

from bookshelf.models import Book
book = Book.objects.get(title='1984')
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Publication Year: {book.publication_year}")

Expected Output:
The output shows the details of the book, confirming that it was successfully retrieved from the database.

>>> book = Book.objects.get(title='1984')
>>> print(f"Title: {book.title}")
Title: 1984
>>> print(f"Author: {book.author}")
Author: George Orwell
>>> print(f"Publication Year: {book.publication_year}")
Publication Year: 1949

3. Update Operation
Command:
To update the book's title, first retrieve the object, then modify the title attribute, and finally call .save().

from bookshelf.models import Book
book_to_update = Book.objects.get(title='1984')
book_to_update.title = 'Nineteen Eighty-Four'
book_to_update.save()
print(book_to_update.title)

Expected Output:
The expected output shows the updated title of the book, confirming the change was saved.

>>> book_to_update = Book.objects.get(title='1984')
>>> book_to_update.title = 'Nineteen Eighty-Four'
>>> book_to_update.save()
>>> print(book_to_update.title)
Nineteen Eighty-Four

4. Delete Operation
Command:
To delete the book instance, retrieve the object and call the .delete() method. To confirm deletion, attempt to retrieve the book again; this will result in a DoesNotExist exception.

from bookshelf.models import Book
book_to_delete = Book.objects.get(title='Nineteen Eighty-Four')
book_to_delete.delete()

# Confirm deletion by trying to retrieve the book again.
try:
    Book.objects.get(title='Nineteen Eighty-Four')
except Book.DoesNotExist:
    print("Book has been successfully deleted.")

Expected Output:
The output will show that the book was successfully deleted, as the DoesNotExist exception was caught.

>>> book_to_delete = Book.objects.get(title='Nineteen Eighty-Four')
>>> book_to_delete.delete()
(1, {'bookshelf.Book': 1})
>>> try:
...     Book.objects.get(title='Nineteen Eighty-Four')
... except Book.DoesNotExist:
...     print("Book has been successfully deleted.")
... 
Book has been successfully deleted.