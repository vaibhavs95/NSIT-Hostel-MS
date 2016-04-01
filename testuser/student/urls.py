from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^$',views.studentProfile, name='student-home'),
    url(r'^(?P<student_id>[a-zA-Z0-9]*)/$',views.completeStudent,name='studentid'),
    url(r'^(?P<student_name>[a-zA-Z0-9]*)/(?P<student_id>[a-zA-Z0-9]*)/$',views.printPDF, name='print-PDF'),
]