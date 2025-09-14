from django.shortcuts import render
from .models import Book

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


from django.views.generic.detail import DetailView
from .models import Library

# Class-Based View (CBV) for showing library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # <--- corrected path
    context_object_name = 'library'




# .....................................

from django.shortcuts import render
from .models import Book
from django.http import HttpResponse

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})


# .....................................

from django.views.generic.detail import DetailView
from .models import Library

# Class-based view to show library details and its books
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
