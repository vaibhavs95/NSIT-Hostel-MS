from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^branch/$',views.addbranch, name='chief_branch'),
    url(r'^$',views.home, name='chiefwarden-home'),
    url(r'^notices/$',views.notices, name='chiefwarden-notices'),
    url(r'^deletenotice/(?P<target>[0-9a-zA-Z]*)/$', views.delNotice , name = 'chiefwarden-delnotice'),
    url(r'^delete/(?P<target>[0-9a-z]*)/$',views.delete_hos,name = 'hos_delete'),
]