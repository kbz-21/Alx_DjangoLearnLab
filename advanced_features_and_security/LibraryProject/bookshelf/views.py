from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from .models import Book

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    return HttpResponse("Create Book Page (only Editors/Admins)")

@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return HttpResponse(f"Edit {book.title} (only Editors/Admins)")

@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return HttpResponse(f"Delete {book.title} (only Admins)")




# ......................................
from django.db.models import Q
from .models import Book

def search_books(request):
    query = request.GET.get("q", "")
    books = Book.objects.filter(Q(title__icontains=query))
    return render(request, "bookshelf/book_list.html", {"books": books})
