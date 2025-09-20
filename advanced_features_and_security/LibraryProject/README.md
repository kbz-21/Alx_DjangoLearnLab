# LibraryProject

This is the first Django project created for the **ALX Introduction to Django task**.

## Project Setup Steps
1. Installed Python and Django.
2. Created a new Django project named **LibraryProject** inside the `Introduction_to_Django` directory.
3. Ran the development server successfully at `http://127.0.0.1:8000/`.
4. Verified the default Django welcome page.

## Project Structure



<!-- ...................................
 -->

 # Permissions and Groups Setup

## Custom Permissions
Defined in `bookshelf/models.py`:
- can_view
- can_create
- can_edit
- can_delete

## Groups
- **Viewers**: can_view
- **Editors**: can_view, can_create, can_edit
- **Admins**: all permissions

## Usage in Views
Views are protected with `@permission_required`. Example:
```python
@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, pk):
    ...

