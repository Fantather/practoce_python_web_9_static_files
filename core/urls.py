
from django.urls import path

from core import views

urlpatterns = [
    path('', views.index, name="main_page"),
    path('contacts/', views.get_contacts, name="contacts_page")
]