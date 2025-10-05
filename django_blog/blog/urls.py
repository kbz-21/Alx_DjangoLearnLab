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
    PostSearchView,
)
from . import views
from .views import CommentCreateView

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
    # path("posts/<int:post_id>/comments/new/", add_comment, name="comment_create"),
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),

    path("comment/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment_delete"),

     path('search/', PostSearchView.as_view(), name='post-search'),
    path('tags/<slug:tag_slug>/', PostListView.as_view(), name='posts-by-tag'),  # filtered by tag
]
