from django.shortcuts import render
from .models import Item
from taggit.models import Tag
from newsapi.serializers import ItemSerializer
from rest_framework.generics import ListAPIView
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView
from django.urls import reverse
from django.db.models import Q






class TagMixin(object):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = Tag.objects.all()
        return context


class IndexView(TagMixin, ListView):
    model = Item
    template_name = "home/index.html"
    paginate_by = 30

    def get_queryset(self):
        queryset = Item.parents.get_stories().prefetch_related('tags').all()
        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) | 
                Q(text__icontains=search_query)  
            )
        return queryset

class TagIndexView(TagMixin, ListView):
    model = Item
    template_name = "home/index.html"
    paginate_by = 30

    def get_queryset(self):
        queryset = Item.parents.get_stories().prefetch_related('tags').filter(tags__slug=self.kwargs.get("tag_slug"))
        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) | 
                Q(text__icontains=search_query)  
            )
        return queryset



class CommentsView(DetailView):
    model = Item
    template_name = "home/comments.html"
    context_object_name = "item"

    def get_object(self, queryset=None):
        item_id = self.kwargs.get('item_id')
        
        if item_id is not None:
            return Item.objects.filter(item_id=item_id).first()
        else:
            return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = Item.comments.get_comments().filter(parent_id=self.object.item_id)
        return context








