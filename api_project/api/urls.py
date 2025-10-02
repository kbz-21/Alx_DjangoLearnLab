

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet


urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]


# Create a router and register the BookViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Task 1: simple list endpoint
    path('books/', BookList.as_view(), name='book-list'),

    # Task 2: full CRUD endpoints
    path('', include(router.urls)),
]
