from rest_framework import serializers
from news.models import Item

class ItemSerializer (serializers.ModelSerializer):
    comment_count = serializers.SerializerMethodField()


    class Meta:
        model = Item
        fields = ("id", "item_id", "item_type", "author", "time", "url", "title", "text", "score", "parent_id", "comment_count")
        read_only_fields = ("fetched",) 

    def get_comment_count(self, obj):
        if obj.item_type == "story" or obj.item_type == "poll":
            comments = Item.objects.filter(parent_id=obj.item_id)
            return comments.count()
        return None