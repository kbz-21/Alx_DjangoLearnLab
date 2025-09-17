from django.contrib import admin
from .models import Book

# Customize the admin interface
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # columns to show
    search_fields = ('title', 'author')  # enable search
    list_filter = ('publication_year',)  # enable filter by publication year

# Register the model with the admin site
admin.site.register(Book, BookAdmin)
