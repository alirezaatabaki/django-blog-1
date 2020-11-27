from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView

from .models import Article, Category


# def home(request, page=1):
#     articles_list = Article.objects.published()
#     paginator = Paginator(articles_list, 3)
#     articles = paginator.get_page(page)
#     context = {
#         'articles': articles,
#     }
#     return render(request, 'blog/article_list.html', context=context)

class ArticleList(ListView):
    queryset = Article.objects.published()
    # context_object_name = "articles"
    paginate_by = 3


# def detail(request, slug):
#     context = {
#         'article': get_object_or_404(Article.objects.published(), slug=slug, status='p')
#     }
#     return render(request, 'blog/article_detail.html', context=context)

class ArticleDetail(DetailView):
    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Article.objects.published(), slug=slug)


# def category(request, slug, page=1):
#     category = get_object_or_404(Category, slug=slug, status=True)
#     articles_list = category.articles.published()
#     paginator = Paginator(articles_list, 3)
#     articles = paginator.get_page(page)
#     context = {
#         'category': category,
#         'articles': articles
#     }
#     return render(request, 'blog/category.html', context=context)

class CategoryList(ListView):
    paginate_by = 3
    template_name = 'blog/category_list.html'

    def get_queryset(self):
        global category
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Category.objects.active(), slug=slug)
        return category.articles.published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = category
        return context