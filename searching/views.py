from django.shortcuts import render, HttpResponse
from django.core import serializers
from .models import *
from django import template
from .tasks import *
from django.db.models import Q

register = template.Library()


def category_counter_func():
    categories = Category.objects.all()
    counts = []
    for i in categories.values():
        counts.append(Subject.objects.filter(category__name=i['name']).count())
    return zip(categories, counts)


def home(request):
    subjects = Subject.objects.all()
    articles = Article.objects.all().order_by('-id')
    categories = category_counter_func()
    context = {'categories': categories, 'subjects': subjects, 'articles': articles[:11]}
    return render(request, 'home.html', context)


def articles_page(request, slug, slug2):
    articles = Article.objects.filter(subject__slug=slug2)
    categories = category_counter_func()
    context = {'articles': articles, 'categories': categories}
    return render(request, 'articles.html', context)


def article_detail(request, slug):
    categories = category_counter_func()
    article = Article.objects.get(slug=slug)
    context = {'categories': categories, 'article': article}
    return render(request, 'article_detail.html', context)


def search_articles(request):
    q = request.GET.get('q')
    articles = Article.objects.filter(
        Q(name__icontains=q) |
        Q(subject__name__icontains=q)
    )
    data = serializers.serialize('json', articles)
    return HttpResponse(data, content_type="application/json")


def count_downloads(request):
    slug = request.GET['slug']
    article = Article.objects.get(slug=slug)
    article.downloads += 1
    article.save()
    return HttpResponse(True)


def sizify(value):
    """
    Simple kb/mb/gb size snippet for templates:
    
    {{ product.file.size|sizify }}
    """
    #value = ing(value)
    if value < 512000:
        value = value / 1024.0
        ext = 'kb'
    elif value < 4194304000:
        value = value / 1048576.0
        ext = 'mb'
    else:
        value = value / 1073741824.0
        ext = 'gb'
    return '%s %s' % (str(round(value, 2)), ext)

register.filter('sizify', sizify)