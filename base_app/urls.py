from django.conf.urls import patterns, url

from base_app import views

urlpatterns = patterns('', url(r'^$', views.index, name='index'))