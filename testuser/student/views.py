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
    alpha =  str(base64.b64decode(student_id))
    alpha = alpha[2:-1]
    u = Students.objects.get(username= alpha)
    a=Hostels.objects.all();
    b=[]
    for i in a:
        d={'name':i.hostel_name,'id':i.username}
        b.append(d)
    if re.match("[0-9]+-[a-zA-Z0-9]*",alpha)!=None:
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
                prev = None
                crimi = None
                try:
                    prev = PreviousHostelDetail.objects.filter(student = alpha)
                except ObjectDoesNotExist:
                    pass
                try:
                    crimi = CriminalRecord.objects.filter(student = alpha)
                except ObjectDoesNotExist:
                    pass
                data = {'all_hostels': b,'student':'yes', 'username': student_id, 's': u,'prev':prev,'crim':crimi}
                return render(request,'student/students/studentProfile.html',data)
            else:
                data = {'form': f, 'all_hostels': b,'student':None, 'username': student_id}
                return render(request,'student/students/home.html',data)

        else:
            u = Students.objects.get(username=alpha)
            prev = None
            crimi = None
            try:
                prev = PreviousHostelDetail.objects.filter(student = alpha)
            except ObjectDoesNotExist:
                pass
            try:
                crimi = CriminalRecord.objects.filter(student = alpha)
            except ObjectDoesNotExist:
                pass
            data = {'all_hostels': b,'student':'yes', 'username': student_id, 's': u,'prev':prev,'crim':crimi}
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
    alpha = alpha[2:-1]
    u = Students.objects.get(username=alpha)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Student Profile.pdf"'

    p = canvas.Canvas(response)


    filename = "logo.png"   # Adding LOGO
    path = settings.MEDIA_ROOT + "/" + str(filename)
    p.drawImage(path, 40, 760, 1*inch, 1 * inch)


    if u.student_photo:
        path = settings.MEDIA_ROOT
        path = path[:-6]
        path = path + u.student_photo.url
    else:
        path = settings.MEDIA_ROOT+"/"+"demo.png"
    p.drawImage(path, 400, 630, 2*inch, 2 * inch)

    p.setFont('Helvetica-Bold', 20)
    p.drawString(180, 800, "STUDENT INFO")

    p.setFont('Helvetica', 8)
    p.drawString(200, 780, "Hostel Management System")

    p.drawString(50, 750, "Roll Number:")
    p.drawString(270, 750, "%s" %u.username)

    p.drawString(50, 730, "Name:")
    p.drawString(270, 730, "%s" %u.name)

    if u.room_number:
        p.drawString(50, 710, "Hostel:")
        p.drawString(270, 710, "%s" %u.room_number.hostel.hostel_name)

        p.drawString(50, 690, "Room Number:")
        p.drawString(270, 690, "%s" %u.room_number)    
    else:
        p.drawString(50, 710, "Hostel:")
        p.drawString(270, 710, "None")

        p.drawString(50, 690, "Room Number:")
        p.drawString(270, 690, "None")

    p.drawString(50, 670, "Date of Birth:")
    p.drawString(270, 670, "%s" %u.date_of_birth)

    p.drawString(50, 650, "Distance from nsit:")
    p.drawString(270, 650, "%s" %u.distance_from_nsit)

    p.drawString(50, 630, "Gender:")
    p.drawString(270, 630, "%s" %u.gender)

    p.drawString(50, 610, "College Category:")
    p.drawString(270, 610, "%s" %u.college_category)

    p.drawString(50, 590, "Blood Group:")
    p.drawString(270, 590, "%s" %u.blood_group)

    p.drawString(50, 570, "Phone Number:")
    p.drawString(270, 570, "%s" %u.student_phone_num)

    p.drawString(50, 550, "Optional Phone Number:")
    p.drawString(270, 550, "%s" %u.student_optional_phone_num)

    p.drawString(50, 530, "Father's Name:")
    p.drawString(270, 530, "%s" %u.father_name)

    p.drawString(50, 510, "Mother's Name:")
    p.drawString(270, 510, "%s" %u.mother_name)

    p.drawString(50, 490, "Parent's Phone Number:")
    p.drawString(270, 490, "%s" %u.parent_phone_num)

    p.drawString(50, 470, "Parent's Optional Phone Number:")
    p.drawString(270, 470, "%s" %u.parent_optional_phone_num)

    p.drawString(50, 450, "Permanent Address:")
    p.drawString(270, 450, "%s" %u.permanent_address)

    p.drawString(50, 430, "Permanent Address Zipcode:")
    p.drawString(270, 430, "%s" %u.permanent_address_zipcode)

    p.drawString(50, 410, "Local Guardian Name:")
    p.drawString(270, 410, "%s" %u.local_guardian_name)

    p.drawString(50, 390, "Local Guardian Address:")
    p.drawString(270, 390, "%s" %u.local_guardian_address)

    p.drawString(50, 370, "Local Guardian Address Zipcode:")
    p.drawString(270, 370, "%s" %u.local_guardian_address_zipcode)

    p.drawString(50, 350, "Local Guardian Phone Number:")
    p.drawString(270, 350, "%s" %u.local_guardian_phone_num)

    p.drawString(50, 330, "Local Guardian Optional Phone Number:")
    p.drawString(270, 330, "%s" %u.local_guardian_optional_phone_num)

    p.drawString(50, 310, "Local Guardian Email:")
    p.drawString(270, 310, "%s" %u.local_guardian_email)

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response
