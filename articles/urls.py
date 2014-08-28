from django.conf.urls import include, patterns, url

urlpatterns = patterns('articles.views',
    url(r'^$', 'articles'),
    url(r'^(?P<article_id>\d+)/$', 'article'),
)
