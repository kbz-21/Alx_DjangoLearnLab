Blog Post Management Features
- List posts: GET /posts/
- View post: GET /posts/<pk>/
- Create post: GET/POST /posts/new/  (login required)
- Edit post: GET/POST /posts/<pk>/edit/  (author only)
- Delete post: POST /posts/<pk>/delete/ (author only)

Author is assigned automatically from logged-in user. Use Django admin or register user via /register/ and login.
All forms include CSRF tokens. Use LoginRequiredMixin and UserPassesTestMixin for access control.
