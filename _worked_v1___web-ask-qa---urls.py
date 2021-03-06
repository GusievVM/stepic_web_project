"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from qa import views

urlpatterns = patterns (
    #v 1
    #url(r'^$', views.home, name='home'),
    #v 2
    #url(r'^$', 'home', name='home'),
    #v4
    # url(r'^$', views.viewsindex, name='viewsindex'),
    'qa.views',
    url(r'^$', views.someview, name='someview'),
    url(r'^login/', views.someview, name='someview'),
    url(r'^signup/', views.someview, name='someview'),
    url(r'^question/([\d]+[\d]+[\d])/', views.someview, name='someview'),
    url(r'^ask/', views.someview, name='someview'),
    url(r'^popular/', views.someview, name='someview'),
    url(r'^new/', views.someview, name='someview'),
    # url(r'^new/.*', test),
)
