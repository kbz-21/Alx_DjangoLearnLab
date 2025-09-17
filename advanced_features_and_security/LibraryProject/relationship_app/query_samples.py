from relationship_app.models import Author, Book, Library, Librarian

# -----------------------------
# 1️⃣ Query all books by a specific author
# -----------------------------
author = Author.objects.create(name="George Orwell")

book1 = Book.objects.create(title="1984", author=author)
book2 = Book.objects.create(title="Animal Farm", author=author)

# QuerySet output (ALX expects QuerySet, not list)
author_books = Book.objects.filter(author=author)
print("Books by George Orwell:", author_books)
# Expected output:
# <QuerySet [<Book: 1984 by George Orwell>, <Book: Animal Farm by George Orwell>]>

# -----------------------------
# 2️⃣ List all books in a library
# -----------------------------
library = Library.objects.create(name="Central Library")
library.books.add(book1, book2)

library_books = library.books.all()
print("Books in Central Library:", library_books)
# Expected output:
# <QuerySet [<Book: 1984 by George Orwell>, <Book: Animal Farm by George Orwell>]>

# -----------------------------
# 3️⃣ Retrieve the librarian for a library
# -----------------------------
librarian = Librarian.objects.create(name="Alice", library=library)

library_librarian = library.librarian
print("Librarian of Central Library:", library_librarian)
# Expected output:
# Alice
