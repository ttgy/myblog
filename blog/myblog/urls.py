from django.conf.urls import url

from . import views


app_name = 'myblog'
urlpatterns = [
    url(r'^$',views.index,name='index'),
    # url(r'^detail/(\d+)/$',views.detail,name='detail'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    #归档连接
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
    url(r'^aaa/$',views.aaa,name='aaa'),
]

