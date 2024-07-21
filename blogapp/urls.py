from django.urls import path
from .views import (
    PostListCreateAPIView,
    PostDetailAPIView,
    CommentListCreateAPIView,
    like_post
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('posts/', PostListCreateAPIView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostDetailAPIView.as_view(), name='post-detail'),
    path('posts/<int:post_pk>/comments/', CommentListCreateAPIView.as_view(), name='comment-list-create'),
    path('posts/<int:pk>/like/', like_post, name='like-post'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
