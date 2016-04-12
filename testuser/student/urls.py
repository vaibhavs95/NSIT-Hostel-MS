from django.conf.urls import url

from . import views,views1

urlpatterns = [
    # url(r'^$',views.studentProfile, name='student-home'),
    url(r'^complaint/$',views1.MakeComplaint,name = 'StudentMakeComplaint'),
    url(r'^(?P<student_id>[0-9]+-[A-Z]+-[0-9]+)/$',views.completeStudent,name='studentid'),  
]