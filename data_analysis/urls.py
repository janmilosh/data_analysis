from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'data_analysis.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', 'stocks.views.hello'),
    url(r'^hello_template/$', 'stocks.views.hello_template'),
)