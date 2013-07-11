from django.conf.urls import patterns, url
from server import views

urlpatterns = patterns('',
    url('^rpc/$', views.rpc, name='rpc'),
    url('^rest/$', views.rest, name='rest'),
)