from django.db import models
from .managers import ItemManager, CommentManager
from taggit.managers import TaggableManager


class Item(models.Model):
    
    objects = models.Manager()  # Default manager
    parents = ItemManager()
    comments = CommentManager()
   

    item_id = models.IntegerField()
    item_type = models.CharField(max_length=50, db_index=True)
    author = models.CharField(max_length=100, null=True)
    time = models.DateTimeField(editable=True, auto_now_add=True)
    url = models.URLField(max_length=500, null=True)
    title = models.CharField(max_length=200, null=True)
    text = models.TextField(null=True)
    score = models.BigIntegerField(default=0, null=True)
    parent_id = models.IntegerField(null=True)
    fetched =  models.BooleanField(default=False)

    tags = TaggableManager()



    class Meta:
        verbose_name = "All Items"
        verbose_name_plural = "All Items"
        ordering = ['-time']

    def __str__(self) -> str:
       if self.title:
          return f'{self.id} - {self.title} - {self.item_type}'
       return f'{self.id} - {self.item_type}'

    @property
    def comment_count(self):
        if self.item_type in ["story", "poll"]:
            comments = Item.objects.filter(parent_id=self.item_id)
            return comments.count()
        
    
    def save(self, *args, **kwargs):
        
        super().save(*args, **kwargs)

        # Add tags based on self.item_type
        if self.item_type == "story":
            self.tags.add("story")
        elif self.item_type == "job":
            self.tags.add("job")
        elif self.item_type == "poll":
            self.tags.add("poll")

    
