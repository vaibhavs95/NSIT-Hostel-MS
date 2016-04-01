from django.conf.urls import url

from . import views,views1

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
    url(r'^council/$',views.council, name='warden-council'),
    url(r'^council/add-council/$',views.addcouncil, name='warden-add-council'),
    url(r'^council/edit-council/(?P<pk>[0-9]+)/$',views.editcouncil, name='warden-edit-council'),
    url(r'^council/delete-council/(?P<pk>[0-9]+)$',views.deletecouncil, name='warden-delete-council'),
    url(r'^hosform/$',views.hosform, name='warden-hosform'),
    url(r'^hosform/add-hosform/$',views.addhosform, name='warden-add-hosform'),
    url(r'^hosform/edit-hosform/(?P<pk>[0-9]+)/$',views.edithosform, name='warden-edit-hosform'),
    url(r'^hosform/delete-hosform/(?P<pk>[0-9]+)$',views.deletehosform, name='warden-delete-hosform'),
    url(r'^mess/$',views.mess, name='warden-mess'),
    url(r'^mess/add-mess/$',views.addmess, name='warden-add-mess'),
    url(r'^mess/edit-mess/(?P<pk>[0-9]+)/$',views.editmess, name='warden-edit-mess'),
    url(r'^deletenotice/(?P<target>[0-9a-zA-Z]*)/$', views1.delNotice , name = 'WardenDelNotice'),
    url(r'^notices/$',views1.notices, name='warden-notices'),
    url(r'^remstudent/(?P<target>[0-9A-Z-]*)/$',views1.remstudent, name='wardenRemoveStudent'),
]