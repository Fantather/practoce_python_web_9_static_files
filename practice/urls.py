from django.urls import path

from practice import views


urlpatterns = [
    path('', views.index, name="main_page"),
    path('details/<int:id>', views.news_details, name='details')
]