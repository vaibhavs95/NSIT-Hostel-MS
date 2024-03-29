from django.conf.urls import url

from . import views,views1

urlpatterns = [
    url(r'^$',views.home, name='warden-home'),
    url(r'^profile-edit/$',views.profileedit, name='warden-profile-edit'),
    url(r'^main-page-edit/$',views.mainpageedit, name='warden-mainpage-edit'),
    #url(r'^profile-edit/$',views.profileedit, name='warden-profile-edit'),
    #room
    url(r'^room/$',views.room, name='warden-room'),
    url(r'^room/all/$',views.roomall, name='warden-room-full'),
    url(r'^room/add/$',views.addroom, name='warden-add-room'),
    url(r'^room/search/$',views.searchroom, name='warden-search-room'),
    url(r'^room/delete/(?P<pk>[0-9]+)$',views.deleteroom, name='warden-delete-room'),
    #facilities
    url(r'^facilities/$',views.facilities, name='warden-facilities'),
    url(r'^facilities/add/$',views.addfacility, name='warden-add-facility'),
    url(r'^facilities/edit/(?P<pk>[0-9]+)/$',views.editfacility, name='warden-edit-facility'),
    url(r'^facilities/delete/(?P<pk>[0-9]+)$',views.deletefacility, name='warden-delete-facility'),
    #council
    url(r'^council/$',views.council, name='warden-council'),
    url(r'^council/add/$',views.addcouncil, name='warden-add-council'),
    url(r'^council/edit/(?P<pk>[0-9]+)/$',views.editcouncil, name='warden-edit-council'),
    url(r'^council/delete/(?P<pk>[0-9]+)/$',views.deletecouncil, name='warden-delete-council'),
    #form
    url(r'^hosform/$',views.hosform, name='warden-hosform'),
    url(r'^hosform/add/$',views.addhosform, name='warden-add-hosform'),
    url(r'^hosform/edit/(?P<pk>[0-9]+)/$',views.edithosform, name='warden-edit-hosform'),
    url(r'^hosform/delete/(?P<pk>[0-9]+)$',views.deletehosform, name='warden-delete-hosform'),
    #mess
    url(r'^mess/$',views.mess, name='warden-mess'),
    url(r'^mess/add/$',views.addmess, name='warden-add-mess'),
    url(r'^mess/edit/(?P<pk>[0-9]+)/$',views.editmess, name='warden-edit-mess'),
    url(r'^deletenotice/(?P<target>[0-9a-zA-Z]*)/$', views1.delNotice , name = 'WardenDelNotice'),
    url(r'^activatenotice/(?P<target>[0-9a-zA-Z]*)/$', views1.activateNotice , name = 'WardenactivateNotice'),
    url(r'^notices/$',views1.notices, name='warden-notices'),
    url(r'^payfine/(?P<primkey>[0-9a-zA-Z]*)/(?P<stu>[0-9A-Za-z-]*)/$',views1.payfine,name='WardenPayFine'),
    url(r'^editPayment/(?P<primkey>[0-9a-zA-Z]*)/(?P<stu>[0-9A-Za-z-]*)/$',views1.editPayment,name='WardenEditPayment'),
    #student
    url(r'^student/$',views.student, name='warden-student'),
    url(r'^student/all/$',views.studentall, name='warden-student-full'),
    url(r'^student/add/$',views.addstudent, name='warden-add-student'),
    url(r'^student/edit/(?P<student>[0-9]+-[A-Z]+-[0-9]+)/$',views.editstudent, name='warden-edit-student'),
    url(r'^student/search/rollno/$',views.searchstudentrollno, name='warden-search-student-rollno'),
    url(r'^student/search/other/$',views.searchstudentother, name='warden-search-student-other'),
    url(r'^student/attach/(?P<student>[0-9]+-[A-Z]+-[0-9]+)/$',views.attachstudent, name='warden-attach-student'),
    url(r'^defaulters/$',views1.viewDefaulters, name='wardenViewDefaulters'),
    url(r'^student/delete/(?P<target>[a-z0-9A-Z-=]*)/$',views1.remstudent, name='wardenRemoveStudent'),
    url(r'^student/profile/(?P<student>[0-9]+-[A-Z]+-[0-9]+)/$',views1.StudentProfile,name='WardenViewStudentProfile'),
    url(r'^student/studentlist/$',views.printStudentList, name='print-stu-list'),
    url(r'^student/roomlist$',views.printRoomList, name='print-room-list'),
    url(r'^detach/(?P<target>[0-9A-Z-]*)/$',views1.detachStudent,name = 'wardenDetachStudent'),
    url(r'^disciplineadd/(?P<target>[0-9A-Z-]*)/$',views1.addCriminalRecord,name = 'wardenAddCriminal'),
    #complaints
    url(r'^complaint/$',views1.ViewComplaint, name='wardenViewComplaint'),
    url(r'^complaint/forward/(?P<pk>[0-9]+)/$',views.forwardcomplaint, name='warden-forward-complaint'),
    url(r'^complaint/(?P<target>[0-9]*)/$',views1.CloseComplaint, name='wardenCloseComplaint'),
    #event
    url(r'^event/$',views.event, name='warden-event'),
    url(r'^event/add/$',views.addevent, name='warden-add-event'),
    url(r'^event/delete/(?P<pk>[0-9]+)/$',views.deleteevent, name='warden-delete-event'),
    url(r'^event/view/(?P<pk>[0-9]+)/$',views.viewevent, name='event-view'),
    url(r'^student/(?P<student_id>[0-9]+-[A-Z]+-[0-9]+)/$',views.printStuDetails, name='print-stu-details'),
    url(r'^student/defaulterslist$',views.printDefaultersList, name='print-defaulters-list'),
]
