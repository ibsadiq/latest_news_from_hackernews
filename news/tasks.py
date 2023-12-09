import datetime
import requests
from django.utils.timezone import make_aware
from .models import Item
from celery import shared_task


BASE_URL = "https://hacker-news.firebaseio.com/v0"

def fetch_items(url):
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()
    

@shared_task
def save_to_db(news_ids, limit=100):
    if not news_ids:
        return

    latest_news_ids = max(news_ids)
    exists = Item.objects.filter(item_id=latest_news_ids).exists()

    if exists:
        return

    news_ids = (list(news_ids))[:limit]

    for news_id in news_ids:
        news_detail = fetch_items(f"{BASE_URL}/item/{news_id}.json")
        news_vals, keys = get_keys(news_detail)
        item_type = news_vals["item_type"]

        if not Item.objects.filter(item_id=news_id).exists():

            # Create an instance of the Items model for each news item
            try:
                Item.objects.create(**news_vals)

                if item_type in ("story", "poll"):
                    fetch_children(item_type, keys[0], news_id)
            except Exception as e:
                print(e, "failed to fetch")
                pass
@shared_task
def fetch_children(item_type, kids, parent_id):
    if not kids:
        return

    for child_id in kids:

        if not Item.objects.filter(item_id=child_id).exists():
            child_detail = fetch_items(f"{BASE_URL}/item/{child_id}.json")
            child_vals, child_keys = get_keys(child_detail)
            child_item_type = child_vals["item_type"]

            # Create an instance of the Items model for each child item
            try:
                child_vals["parent_id"] = parent_id
                Item.objects.create(**child_vals)

                if child_item_type in ("story", "poll"):
                    fetch_children(child_item_type, child_keys[0], child_id)
            except Exception as e:
                print(e, "failed to fetch")
                pass

@shared_task
def get_keys(news_detail):
    item_type = news_detail.get("type")
    item_id = str(news_detail.get("id"))
    author = news_detail.get("by")
    time = news_detail.get("time")
    time = make_aware(datetime.datetime.fromtimestamp(time))
    url = news_detail.get("url")
    title = news_detail.get("title")
    text = news_detail.get("text")
    score = news_detail.get("score", 0)
    kids = list(reversed(sorted(news_detail.get("kids", []))))
    parts = news_detail.get("parts", [])  # pollopt
    vals = {
        "item_type": item_type,
        "item_id": item_id,
        "author": author,
        "time": time,
        "url": url,
        "title": title,
        "text": text,
        "score": score,
        "fetched":True
        
    }
    return vals, (kids, parts)


@shared_task
def new_items():
    news_ids = (fetch_items(f'{BASE_URL}/askstories.json')+fetch_items(f'{BASE_URL}/topstories.json')
                +fetch_items(f'{BASE_URL}/jobstories.json'))
    news_ids = set(news_ids)
    save_to_db(news_ids)


@shared_task
def get_latest_news():
    new_items.delay()

