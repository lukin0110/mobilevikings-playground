from django.conf.urls import patterns, url
from server import views_rpc, views_rest

urlpatterns = patterns('',
    url('^xmlrpc/$', views_rpc.xmlrpc, name='xmlrpc'),

    url('^rest/$', views_rest.overview, name='rest.overview'),
    url('^rest/ping$', views_rest.PingView.as_view(), name='rest.ping'),
    url('^rest/balance$', views_rest.BalanceView.as_view(), name='rest.balance'),
    url('^rest/portin$', views_rest.PortinView.as_view(), name='rest.portin'),
    url('^rest/portout$', views_rest.PortoutView.as_view(), name='rest.portout'),
    url('^rest/addcredit$', views_rest.AddcreditView.as_view(), name='rest.addcredit'),
)
