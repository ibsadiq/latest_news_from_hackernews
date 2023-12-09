from rest_framework import viewsets
from news.models import Item
from .serializers import ItemSerializer
from .permissions import CanDeleteItem,  CanUpdateItem

class StoryViewSet(viewsets.ModelViewSet):
    queryset = Item.parents.get_stories().all()
    serializer_class = ItemSerializer
    permission_classes = [CanDeleteItem, CanUpdateItem]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Item.comments.get_comments().all()
    serializer_class = ItemSerializer
    permission_classes = [CanDeleteItem, CanUpdateItem]

