from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    add_comment,
    CommentUpdateView,
    CommentDeleteView,
)
from . import views

urlpatterns = [
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("profile/", views.profile_view, name="profile"),
    path("posts/", PostListView.as_view(), name="posts_list"),            # list
    path("post/new/", PostCreateView.as_view(), name="post_create"),     # create
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),# detail
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post_update"),  # ✅ update
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"), # d

     # Comment URLs
    path("posts/<int:post_id>/comments/new/", add_comment, name="comment_create"),
    path("comments/<int:pk>/edit/", CommentUpdateView.as_view(), name="comment_edit"),
    path("comments/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment_delete"),
]
