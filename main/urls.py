from django.conf.urls import url

from . import views


app_name = 'main' 
#This sets application namespace to diffretiate urls of different apps.

urlpatterns = [
    #url for home-page:
    url(r'^$', views.index, name='index'),

    #url to Enter a new Topic:
    url(r'^add_topic$', views.addtopic, name='addtopic'),

    #url to Enter a new Topic:
    url(r'^add_opinion$', views.addopinion, name='addopinion'),

    #url to topic page:
    url(r'^(?P<pk>[0-9]+)/topic$', views.TopicView.as_view(), name='topic'),

    #url to search a topic:
    url(r'^search$', views.search, name='search'),
]
