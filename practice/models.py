from itertools import count

from django.db import models


gen_id = count()

# Create your models here.
class News:
    id:int
    static_image_path:str
    title:str
    text:str

    def __init__(self, image_path:str, title:str, text:str) -> None:
        self.id = next(gen_id)
        self.static_image_path = image_path
        self.title = title
        self.text = text


class NewsRepository:
    news:dict[int, News]

    def __init__(self) -> None:
        self.news = {}

    def add(self, new_news:News) -> None:
        self.news[new_news.id] = new_news

    def get_by_id(self, target_id:int) -> News|None:
        return self.news.get(target_id, None)


news_repo = NewsRepository()
news_repo.add(News('assets/hamster_1.jpg', 'News 1', 'Text news 1'))
news_repo.add(News('assets/hamster_2.jpg', 'News 2', 'Text news 2'))
news_repo.add(News('assets/hamster_3.jpg', 'News 3', 'Text news 3'))
news_repo.add(News('assets/hamster_4.jpg', 'News 4', 'Text news 4'))
news_repo.add(News('assets/hamster_5.jpg', 'News 5', 'Text news 5'))
news_repo.add(News('assets/hamster 6.jpg', 'News 6', 'Text news 6'))