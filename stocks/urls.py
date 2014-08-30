from django.conf.urls import include, patterns, url

urlpatterns = patterns('stocks.views',
    url(r'^$', 'stocks'),
    url(r'^(?P<stock_id>\d+)/$', 'stock'),
)
