from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import PostViewSet, CommentViewSet
from .views import FeedListView
from .views import PostLikeView, PostUnlikeView



router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', FeedListView.as_view(), name='user-feed'),
    path('posts/<int:pk>/like/', PostLikeView.as_view(), name='post-like'),
    path('posts/<int:pk>/unlike/', PostUnlikeView.as_view(), name='post-unlike'),
    
]
