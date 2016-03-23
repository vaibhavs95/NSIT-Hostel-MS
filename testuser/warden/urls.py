from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',views.home, name='warden-home'),
    url(r'^profile-edit$',views.profileedit, name='warden-profile-edit'),
    url(r'^room$',views.room, name='warden-room'),
    url(r'^room/addroom$',views.addroom, name='warden-add-room'),
    #url(r'^room/editroom$',views.editroom, name='warden-edit-room'),
    #url(r'^room/deleteroom$',views.deleteroom, name='warden-delete-room'),
    url(r'^student$',views.student, name='warden-student'),
    url(r'^student/addstudent$',views.addstudent, name='warden-add-student'),
    url(r'^facilities/$',views.facilities, name='warden-facilities'),
    url(r'^facilities/add-facility/$',views.addfacility, name='warden-add-facility'),
    url(r'^facilities/edit-facility/(?P<pk>[0-9]+)/$',views.editfacility, name='warden-edit-facility'),
    url(r'^facilities/delete-facility/(?P<pk>[0-9]+)$',views.deletefacility, name='warden-delete-facility'),
]