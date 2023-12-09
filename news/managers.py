from django.db import models


class ItemManager(models.Manager):
    def get_stories(self):
        return self.get_queryset().exclude(item_type__in=["comment", "pollopt"])
    

class CommentManager(models.Manager):
    def get_comments(self):
        return self.get_queryset().filter(item_type__in=["comment", "pollopt"])
    

