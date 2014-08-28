from django.shortcuts import render
from django.shortcuts import get_object_or_404
from articles.models import Article

def articles(request):
    articles = Article.objects.all()

    return render(request, 'articles.html', ({
        'articles': articles
    }))

def article(request, article_id=1):
    article = get_object_or_404(Article, id=article_id)

    return render(request, 'article.html', ({
        'article': article
    }))