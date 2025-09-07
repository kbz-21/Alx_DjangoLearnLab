from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author = Author.objects.create(name="George Orwell")
book1 = Book.objects.create(title="1984", author=author)
book2 = Book.objects.create(title="Animal Farm", author=author)
print("Books by George Orwell:", list(author.books.all()))

# List all books in a library
library = Library.objects.create(name="Central Library")
library.books.add(book1, book2)
print("Books in Central Library:", list(library.books.all()))

# Retrieve the librarian for a library
librarian = Librarian.objects.create(name="Alice", library=library)
print("Librarian of Central Library:", library.librarian)
