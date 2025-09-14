from django.shortcuts import render
from .models import Book


from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

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






# Register view
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto-login after registration
            return redirect('list_books')  # redirect to books page
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Login view
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('list_books')
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

# Logout view
def logout_view(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')
