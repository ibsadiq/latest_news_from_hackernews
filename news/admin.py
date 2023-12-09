from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ["item_type", "author", "title", "url", "parent_id"]
    search_fields = ["title", "item_type", "author", "item_id"]
    list_per_page = 20
    list_filter = [
        "item_type",
    ]
