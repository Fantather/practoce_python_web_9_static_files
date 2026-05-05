from django.http import Http404
from django.shortcuts import render
from .models import News, news_repo

# Create your views here.
def index(request):
    return render(request, "index.html", {'news': news_repo.news.values()})

def news_details(request, id:int):
    target_news = news_repo.get_by_id(id)
    if target_news is None:
        raise Http404
    return render(request, "news_details.html", {
        'title': target_news.title,
        'image_path': target_news.static_image_path,
        'text': target_news.text,
    })