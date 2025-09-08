from bookshelf.models import Book
new_book = Book(title='1984', author='George Orwell', publication_year=1949)
new_book.save()

Expected Output
The output of the save() command will indicate that the object has been successfully created and saved to the database.

# No output is displayed on the console if successful. 
# The command simply returns a new line, indicating success.
# To confirm, you can retrieve the object.
