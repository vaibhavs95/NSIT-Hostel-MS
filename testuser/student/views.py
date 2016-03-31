from django.shortcuts import render
from reportlab.pdfgen import canvas
import re
from django.conf import settings
import base64, os
from django.shortcuts import render,redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from newapp.models import *
# Create your views here.
from .forms import *
@login_required
@require_http_methods(['GET', 'POST'])
def completeStudent(request, student_id):
    alpha =  str(base64.b64decode(student_id))
    alpha = alpha[2:11]
    print (alpha)
    a=Hostels.objects.all();
    b=[]
    for i in a:
        d={'name':i.hostel_name,'id':i.username}
        b.append(d)
    if re.match("[0-9]+-[a-zA-Z0-9]*",alpha)!=None:
        print (request)
        if request.method == 'POST':
            u = Students.objects.get(username = alpha)
            f = CreateStudentForm(request.POST or None, request.FILES, instance = u)
            if f.is_valid():
                if request.FILES.__contains__('student_photo'):
                    ext = request.FILES['student_photo'].name.split('.')[-1]
                    filename = alpha
                    path = settings.MEDIA_ROOT + "/student/images/" + str(filename) + "." + str(ext)
                    try:
                        os.remove(path)
                    except FileNotFoundError:   
                        pass
                    f.student_photo = request.FILES['student_photo']
                f.save()
                data = {'all_hostels': b,'student':'yes', 'username': student_id, 's': u}
                return render(request,'student/students/studentProfile.html',data)
            else:
                data = {'form': f, 'all_hostels': b,'student':None, 'username': student_id}
                return render(request,'student/students/home.html',data)

        else:
            u = Students.objects.get(username=alpha)
            data = {'all_hostels': b,'student':'yes', 'username': student_id, 's': u}
            if (u.distance_from_nsit != 0):
                return render(request,'student/students/studentProfile.html',data)    
            f = CreateStudentForm(instance = u)
            data = {'form': f,'all_hostels': b, 'username': student_id}
            return render(request, 'student/students/home.html',data)
    else:
        return redirect('logout')

def printPDF(request, student_id, student_name):
    print ("Hello")
    alpha =  str(base64.b64decode(student_id))
    alpha = alpha[2:11]
    u = Students.objects.get(username=alpha)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

    p = canvas.Canvas(response)
    p.setFont('Helvetica-Bold', 20)
    p.drawString(180, 800, "Basic Info")

    p.setFont('Helvetica', 8)
    p.drawString(50, 750, "Name:")
    p.drawString(270, 750, "%s" %u.name)

    p.drawString(50, 730, "Date of Birth:")
    p.drawString(270, 730, "%s" %u.date_of_birth)

    p.drawString(50, 710, "Distance from nsit:")
    p.drawString(270, 710, "%s" %u.distance_from_nsit)

    p.drawString(50, 690, "Gender:")
    p.drawString(270, 690, "%s" %u.gender)

    p.drawString(50, 670, "College Category:")
    p.drawString(270, 670, "%s" %u.college_category)

    p.drawString(50, 650, "Blood Group:")
    p.drawString(270, 650, "%s" %u.blood_group)

    p.drawString(50, 630, "Phone Number:")
    p.drawString(270, 630, "%s" %u.student_phone_num)

    p.drawString(50, 610, "Optional Phone Number:")
    p.drawString(270, 610, "%s" %u.student_optional_phone_num)

    p.drawString(50, 590, "Father's Name:")
    p.drawString(270, 590, "%s" %u.father_name)

    p.drawString(50, 570, "Mother's Name:")
    p.drawString(270, 570, "%s" %u.mother_name)

    p.drawString(50, 550, "Parent's Phone Number:")
    p.drawString(270, 550, "%s" %u.parent_phone_num)

    p.drawString(50, 530, "Parent's Optional Phone Number:")
    p.drawString(270, 530, "%s" %u.parent_optional_phone_num)

    p.drawString(50, 510, "Permanent Address:")
    p.drawString(270, 510, "%s" %u.permanent_address)

    p.drawString(50, 490, "Permanent Address Zipcode:")
    p.drawString(270, 490, "%s" %u.permanent_address_zipcode)

    p.drawString(50, 470, "Local Guardian Name:")
    p.drawString(270, 470, "%s" %u.local_guardian_name)

    p.drawString(50, 450, "Local Guardian Address:")
    p.drawString(270, 450, "%s" %u.local_guardian_address)

    p.drawString(50, 430, "Local Guardian Address Zipcode:")
    p.drawString(270, 430, "%s" %u.local_guardian_address_zipcode)

    p.drawString(50, 410, "Local Guardian Phone Number:")
    p.drawString(270, 410, "%s" %u.local_guardian_phone_num)

    p.drawString(50, 390, "Local Guardian Optional Phone Number:")
    p.drawString(270, 390, "%s" %u.local_guardian_optional_phone_num)

    p.drawString(50, 370, "Local Guardian Email:")
    p.drawString(270, 370, "%s" %u.local_guardian_email)

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response

def save_file(file, username, path=''):
    ''' Little helper to save a file
    ''' 
    ext = file.name.split('.')[-1]
    filename = username
    path = settings.MEDIA_ROOT + "/student/" + str(path) + str(filename) + "." + str(ext)  
    fd = open('%s' % (path), 'wb')
    for chunk in file.chunks():
        fd.write(chunk)
    fd.close()