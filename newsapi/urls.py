from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StoryViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'stories', StoryViewSet, basename="stories")
router.register(r'comments', CommentViewSet, basename="comments")

urlpatterns = [
    path('', include(router.urls)),
]