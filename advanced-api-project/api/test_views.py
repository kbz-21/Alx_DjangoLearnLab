from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import Book


class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="testpass123")
        self.token = Token.objects.create(user=self.user)

        # Create sample book
        self.book = Book.objects.create(
            title="Test Book",
            author="John Doe",
            publication_year=2021
        )

        # Endpoints
        self.list_url = reverse("book-list")      # /books/
        self.detail_url = reverse("book-detail", args=[self.book.id])  # /books/<id>/
        self.create_url = reverse("book-create")  # /books/create/
        self.update_url = reverse("book-update", args=[self.book.id])  # /books/update/<id>/
        self.delete_url = reverse("book-delete", args=[self.book.id])  # /books/delete/<id>/

    def authenticate(self):
        """Helper method to authenticate a user with DRF Token."""
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    # ------------------------
    # CRUD Tests
    # ------------------------
    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("title", response.data[0])

    def test_create_book_requires_authentication(self):
        data = {"title": "New Book", "author": "Jane Doe", "publication_year": 2022}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_book_authenticated_with_token(self):
        """Test using Token authentication"""
        self.authenticate()
        data = {"title": "New Book", "author": "Jane Doe", "publication_year": 2022}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_create_book_authenticated_with_login(self):
        """Test using Django's default login session"""
        login = self.client.login(username="testuser", password="testpass123")
        self.assertTrue(login)  # Ensure login was successful
        data = {"title": "Another Book", "author": "Jane Doe", "publication_year": 2023}
        response = self.client.post(self.create_url, data)
        self.assertIn(response.status_code, [status.HTTP_201_CREATED, status.HTTP_302_FOUND])
        # Some APIs may redirect after login, so we allow both

    def test_update_book_authenticated(self):
        self.authenticate()
        data = {"title": "Updated Book", "author": "John Doe", "publication_year": 2021}
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Book")

    def test_delete_book_authenticated(self):
        self.authenticate()
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    # ------------------------
    # Filtering, Search, Ordering
    # ------------------------
    def test_filter_books_by_author(self):
        response = self.client.get(self.list_url, {"author": "John Doe"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books_by_title(self):
        response = self.client.get(self.list_url, {"search": "Test"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any("Test Book" in book["title"] for book in response.data))

    def test_order_books_by_year(self):
        Book.objects.create(title="Older Book", author="Another", publication_year=2000)
        response = self.client.get(self.list_url, {"ordering": "publication_year"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertLessEqual(response.data[0]["publication_year"], response.data[-1]["publication_year"])
