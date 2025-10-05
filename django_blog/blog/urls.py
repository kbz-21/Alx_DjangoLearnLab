from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)
from . import views

urlpatterns = [
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("profile/", views.profile_view, name="profile"),
    path("posts/", PostListView.as_view(), name="posts_list"),            # list
    path("posts/new/", PostCreateView.as_view(), name="post_create"),     # create
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post_detail"),# detail
    path("posts/<int:pk>/edit/", PostUpdateView.as_view(), name="post_edit"),   # edit
    path("posts/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"), # d
]
