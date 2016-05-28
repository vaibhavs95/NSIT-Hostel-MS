from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$',views.base, name='base'),
    url(r'^login/$',views.handleLogin, name='login'),
    url(r'^home/$',views.home, name='home'),
    url(r'^logout/$',views.logoutview, name='logout'),
	url(r'^(?P<hostel_name>[a-z0-9]*warden)/$',views.hostels,name='hostel'),
	url(r'^resetpassword/$',views.resetPassword,name = 'newappResetPassword'),
	url(r'^event/view/(?P<pk>[0-9]+)/$',views.viewevent, name='newapp-event-view'),
	url(r'^team/$',views.team, name='team'),
]