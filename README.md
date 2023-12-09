# HackerNews API Project

## Goals of the project
The goal is to make a web app to make it easier to navigate the news:

Choose a web framework of your choice. Django, Flask, use what you like. Make a new virtualenv and pip install it;
Make a scheduled job to sync the published news to a DB every 5 minutes. You can start with the latest 100 items, and sync every new item from there. Note: here are several types of news (items), with relations between them;
Implement a view to list the latest news;
Allow filtering by the type of item;
Implement a search box for filtering by text
As there are hundreds of news you probably want to use pagination or lazy loading when you display them.
It is also important to expose an API so that our data can be consumed:

GET: List the items, allowing filters to be specified;
POST: Add new items to the database (not present in Hacker News);

Bonus

Only display top-level items in the list, and display their children (comments, for example) on a detail page;
In the API, allow updating and deleting items if they were created in the API (but never data that was retrieved from Hacker News);
Be creative! :)

## To run this project on your local machine, please follow the following steps

1. set up and activate your virtual enviroment
2. Install the dependencies from the requirement.txt
3. Install Redis on your computer, Using sudo snap install redis for Linux. For Mac users download Redis: https://redis.io/download
4. runserver with python manage.py runserver
5.start celery with the command: celery -A core worker -l info
6.start celerybeat with the command: celery -A core beat -l info