from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$',views.base, name='base'),
    url(r'^login/$',views.handleLogin, name='login'),
    url(r'^home/$',views.home, name='home'),
    url(r'^logout/$',views.logoutview, name='logout'),
	url(r'^hostel/(?P<hostel_name>[a-z0-9]*)/$',views.hostels,name='hostel'),
]