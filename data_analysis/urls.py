from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^articles/', include('articles.urls')),
    (r'^stocks/', include('stocks.urls')),
)