from django.conf.urls import patterns, include, url
from stocks.views import HelloTemplate

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'data_analysis.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', 'stocks.views.hello'),
    url(r'^hello_template_simple/$', 'stocks.views.hello_template_simple'),
    url(r'^hello_class_view/$', HelloTemplate.as_view()),
)