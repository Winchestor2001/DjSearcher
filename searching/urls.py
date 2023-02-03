from django.urls import path
from . import views


urlpatterns = [
     path('', views.home, name='home'),
     path('articles/<slug:slug>/<slug:slug2>/', views.articles_page, name='articles'),
     path('article_detail/<slug:slug>/', views.article_detail, name='article_detail'),
     path('search_articles/', views.search_articles, name='search_articles'),
     path('count_downloads/', views.count_downloads, name='count_downloads'),
]