from django.conf.urls import patterns, include, url
from articles.views import HelloTemplate
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'data_analysis.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', 'articles.views.hello'),
    url(r'^hello_template_simple/$', 'articles.views.hello_template_simple'),
    url(r'^hello_class_view/$', HelloTemplate.as_view()),
)