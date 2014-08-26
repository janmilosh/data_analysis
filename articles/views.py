from django.shortcuts import render
from articles.models import Article

def articles(request):
    articles = Article.objects.all()

    return render(request, 'articles.html', ({
        'articles': articles
    }))