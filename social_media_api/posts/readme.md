## Follows & Feed API

- POST /accounts/follow/<user_id>/    (auth required) follow a user
- POST /accounts/unfollow/<user_id>/  (auth required) unfollow a user
- GET  /accounts/<user_id>/following/ list users <user_id> follows
- GET  /accounts/<user_id>/followers/ list followers of <user_id>
- GET  /api/posts/feed/               list posts from users you follow (auth required)

Notes:
- `following` is a ManyToMany field on the user model (symmetrical=False).
- Use token auth header: Authorization: Token <token>
