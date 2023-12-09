# from . import views
from .views import IndexView, CommentsView, TagIndexView

from django.urls import path

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('tags/<slug:tag_slug>/', TagIndexView.as_view(), name="post_by_tag"),
    path('story/<int:item_id>/', CommentsView.as_view(), name='comments'),
]
  