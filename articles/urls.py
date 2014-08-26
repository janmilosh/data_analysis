from django.conf.urls import include, patterns, url

urlpatterns = patterns('',

    url(r'^$', 'articles.views.articles', name='articles'),
)
