from django.shortcuts import render, get_object_or_404

from .models import Article, Category


def home(request):
    context = {
        'articles': Article.objects.published()
    }
    return render(request, 'blog/home.html', context=context)


def detail(request, slug):
    context = {
        'article': get_object_or_404(Article.objects.published(), slug=slug, status='p')
    }
    return render(request, 'blog/detail.html', context=context)


def category(request, slug):
    context = {
        'category': get_object_or_404(Category, slug=slug, status=True)
    }
    return render(request, 'blog/category.html', context=context)
