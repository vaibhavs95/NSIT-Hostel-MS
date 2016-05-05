from django.shortcuts import render
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from django.conf import settings
import base64, os, re
from django.shortcuts import render,redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from newapp.models import *
from reportlab.lib.utils import ImageReader
# Create your views here.
from .forms import *


@login_required
@require_http_methods(['GET', 'POST'])
def completeStudent(request, student_id):
    #alpha =  str(base64.b64decode(student_id))
    #alpha = alpha[2:-1]
    u = Students.objects.get(username= student_id)
    a=Hostels.objects.all();
    b=[]
    for i in a:
        d={'name':i.hostel_name,'id':i.username}
        b.append(d)
    if re.match(str(request.user),student_id)!=None:
        if request.method == 'POST':
            u = Students.objects.get(username = student_id)
            f = CreateStudentForm(request.POST or None, request.FILES, instance = u)
            if f.is_valid():
                if request.FILES.__contains__('student_photo'):
                    ext = request.FILES['student_photo'].name.split('.')[-1]
                    filename = student_id
                    path = settings.MEDIA_ROOT + "/student/images/" + str(filename) + "." + str(ext)
                    try:
                        os.remove(path)
                    except FileNotFoundError:   
                        pass
                    f.student_photo = request.FILES['student_photo']
                f.save()
                deaf = HostelAttachDates.objects.filter(student = u)
                deaf.delete
                prev = None
                crimi = None
                try:
                    prev = PreviousHostelDetail.objects.filter(student = u).order_by('hostel_join_date')
                except ObjectDoesNotExist:
                    pass
                try:
                    crimi = CriminalRecord.objects.filter(student = u).order_by('date_of_action')
                except ObjectDoesNotExist:
                    pass
                payment = None
                try:
                    payment = PaymentDetails.objects.filter(student = u).order_by('paymentDate')
                except ObjectDoesNotExist:
                    pass
                print(payment)
                data = {'all_hostels': b,'student':'yes', 'username': student_id, 's': u,'prev':prev,'crim':crimi,'paym':payment}
                return render(request,'student/students/studentProfile.html',data)
            else:
                data = {'form': f, 'all_hostels': b,'student':None, 'username': student_id}
                return render(request,'student/students/home.html',data)

        else:
            u = Students.objects.get(username=student_id)
            prev = None
            crimi = None
            try:
                prev = PreviousHostelDetail.objects.filter(student = u).order_by('hostel_join_date')
            except ObjectDoesNotExist:
                pass
            try:
                crimi = CriminalRecord.objects.filter(student = u).order_by('date_of_action')
            except ObjectDoesNotExist:
                pass
            payment = None
            try:
                payment = PaymentDetails.objects.filter(student = u).order_by('paymentDate')
            except ObjectDoesNotExist:
                pass
            data = {'all_hostels': b,'student':'yes', 'username': student_id, 's': u,'prev':prev,'crim':crimi,'paym':payment}
            if (u.distance_from_nsit != 0):
                return render(request,'student/students/studentProfile.html',data)    
            f = CreateStudentForm(instance = u)
            data = {'form': f,'all_hostels': b, 'username': student_id}
            return render(request, 'student/students/home.html',data)
    else:
        return redirect('logout')
