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



# .............................................
## HTTPS and Security Settings

- `SECURE_SSL_REDIRECT = True`: Redirects all HTTP requests to HTTPS.
- `SECURE_HSTS_SECONDS = 31536000`: Enforces HTTPS for one year.
- `SECURE_HSTS_INCLUDE_SUBDOMAINS = True`: Applies HSTS to all subdomains.
- `SECURE_HSTS_PRELOAD = True`: Allows site to be included in browser preload lists.
- `SESSION_COOKIE_SECURE = True`: Ensures session cookies are sent only via HTTPS.
- `CSRF_COOKIE_SECURE = True`: Ensures CSRF cookies are sent only via HTTPS.
- `X_FRAME_OPTIONS = "DENY"`: Protects against clickjacking.
- `SECURE_CONTENT_TYPE_NOSNIFF = True`: Prevents MIME sniffing.
- `SECURE_BROWSER_XSS_FILTER = True`: Enables browser XSS filter.

### Deployment
Configured Nginx with SSL (Let’s Encrypt) to serve the application securely.
