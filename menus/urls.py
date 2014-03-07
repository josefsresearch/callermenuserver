from django.conf.urls import patterns, url
from menus import views

urlpatterns = patterns('',
    #ex: /menus/
    url(r'^$', views.home, name='home'),
    #ex: /menus/user/6503195577/
    url(r'^user/(?P<num>\d+)/$', views.is_user, name='is_user'),
    #ex: /menus/menu/123/
    url(r'^menu/(?P<num>\d+)/(?P<lan>\d{1})/$', views.get_menu, name='get_menu'),
)
