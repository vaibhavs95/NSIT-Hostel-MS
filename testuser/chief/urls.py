from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^branch/$',views.addbranch, name='chief_branch'),
    url(r'^$',views.home, name='chiefwarden-home'),
    url(r'^notices/$',views.notices, name='chiefwarden-notices'),
    url(r'^room/$',views.room, name='chiefwarden-room'),
    url(r'^room/search/$',views.searchroom, name='chiefwarden-search-room'),
    url(r'^student/$',views.student, name='chiefwarden-student'),
    url(r'^student/search/rollno/$',views.searchstudentrollno, name='chiefwarden-search-student-rollno'),
    url(r'^student/search/other/$',views.searchstudentother, name='chiefwarden-search-student-other'),
    url(r'^deletenotice/(?P<target>[0-9a-zA-Z]*)/$', views.delNotice , name = 'chiefwarden-delnotice'),
    url(r'^delete/(?P<target>[0-9a-z]*)/$',views.delete_hos,name = 'hos_delete'),
<<<<<<< HEAD
    url(r'^student/profile/(?P<student>[0-9]+-[A-Z]+-[0-9]+)/$',views.StudentProfile,name='chief-student-profile'),
    url(r'^student/fine/add/(?P<student>[0-9]+-[A-Z]+-[0-9]+)/$',views.addfine,name='chief-add-fine'),
    url(r'^student/payfine/(?P<primkey>[0-9]+)/(?P<stu>[0-9]+-[A-Z]+-[0-9]+)/$',views.payfine,name='chief-payfine'),
=======
    url(r'^student/profile/(?P<student>[0-9A-Z-]*/$)',views.StudentProfile,name='ChiefWardenViewStudentProfile'),
    url(r'^addBank/$',views.addBank,name = 'chiefAddBank'),
>>>>>>> 608a2bb0b8ceeac023d91daaaf39bfc47abe378b
]