## Social Media API - Posts & Comments

Endpoints (base /api/):
- GET /posts/                list posts (paginated)
- POST /posts/               create post (auth)
- GET /posts/{id}/           retrieve post (includes nested comments)
- PUT/PATCH /posts/{id}/     update post (owner only)
- DELETE /posts/{id}/        delete post (owner only)

- GET /comments/             list comments
- POST /comments/            create comment (auth) -> payload: {"post": <post_id>, "content": "text"}
- PUT/PATCH /comments/{id}/  update comment (author only)
- DELETE /comments/{id}/     delete comment (author only)

Filtering & search:
- /api/posts/?search=foo
- /api/posts/?ordering=-created_at
- /api/posts/?author__username=username

Auth:
- Token authentication is used. Include header: Authorization: Token <key>
