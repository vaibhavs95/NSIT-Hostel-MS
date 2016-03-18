from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',views.home, name='chiefwarden-home'),
    url(r'^delete/(?P<target>[0-9a-z]*)/$',views.delete_hos,name = 'hos_delete'),
    url(r'^addhostel/$',views.add_hos,name = 'hos_add'),
]