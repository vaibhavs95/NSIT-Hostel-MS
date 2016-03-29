from django.shortcuts import render
import re
import base64
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
    if re.match("[0-9]*-[a-zA-Z0-9]*",alpha)!=None:
        print (request)
        if request.method == 'POST':
            f = CreateStudentForm(request.POST or None)
            if f.is_valid():
                Students.objects.filter(username=alpha).update(name = f.cleaned_data.get('name'), date_of_birth=f.cleaned_data.get('date_of_birth'), distance_from_nsit=f.cleaned_data.get('distance_from_nsit'), gender=f.cleaned_data.get('gender'), college_category=f.cleaned_data.get('college_category'), blood_group=f.cleaned_data.get('blood_group'), student_phone_num=f.cleaned_data.get('student_phone_num'), student_optional_phone_num=f.cleaned_data.get('student_optional_phone_num'),father_name=f.cleaned_data.get('father_name'), mother_name=f.cleaned_data.get('mother_name'),parent_email=f.cleaned_data.get('parent_email'),parent_phone_num=f.cleaned_data.get('parent_phone_num'),parent_optional_phone_num=f.cleaned_data.get('parent_optional_phone_num'), permanent_address=f.cleaned_data.get('permanent_address'), permanent_address_zipcode=f.cleaned_data.get('permanent_address_zipcode'), local_guardian_name=f.cleaned_data.get('local_guardian_name'), local_guardian_address=f.cleaned_data.get('local_guardian_name'), local_guardian_address_zipcode=f.cleaned_data.get('local_guardian_address_zipcode'), local_guardian_phone_num=f.cleaned_data.get('local_guardian_phone_num'), local_guardian_optional_phone_num=f.cleaned_data.get('local_guardian_optional_phone_num'), local_guardian_email=f.cleaned_data.get('local_guardian_email') )
                data = {'all_hostels': b,'student':'yes', 'username': student_id, 'name': f.cleaned_data.get('name'), 'date_of_birth': f.cleaned_data.get('date_of_birth'), 'distance_from_nsit': f.cleaned_data.get('distance_from_nsit'), 'gender': f.cleaned_data.get('gender'), 'college_category':f.cleaned_data.get('college_category'), 'blood_group':f.cleaned_data.get('blood_group'), 'student_phone_num': f.cleaned_data.get('student_phone_num'), 'student_optional_phone_num': f.cleaned_data.get('student_optional_phone_num'),'father_name': f.cleaned_data.get('father_name'), 'mother_name': f.cleaned_data.get('mother_name'),'parent_email': f.cleaned_data.get('parent_email'), 'parent_phone_num': f.cleaned_data.get('parent_phone_num'),'parent_optional_phone_num': f.cleaned_data.get('parent_optional_phone_num'), 'permanent_address': f.cleaned_data.get('permanent_address'), 'permanent_address_zipcode': f.cleaned_data.get('permanent_address_zipcode'), 'local_guardian_name': f.cleaned_data.get('local_guardian_name'), 'local_guardian_address': f.cleaned_data.get('local_guardian_name'), 'local_guardian_address_zipcode': f.cleaned_data.get('local_guardian_address_zipcode'), 'local_guardian_phone_num': f.cleaned_data.get('local_guardian_phone_num'), 'local_guardian_optional_phone_num': f.cleaned_data.get('local_guardian_optional_phone_num'), 'local_guardian_email': f.cleaned_data.get('local_guardian_email') }
                return render(request,'student/students/studentProfile.html',data)
            else:
                data = {'form': f, 'all_hostels': b,'student':None, 'username': student_id}
                return render(request,'student/students/home.html',data)

        else:
            u = Students.objects.get(username=alpha)
            data = {'all_hostels': b,'student':'yes', 'username': student_id, 'name': u.name, 'date_of_birth': u.date_of_birth, 'distance_from_nsit': u.distance_from_nsit, 'gender': u.gender, 'college_category': u.college_category, 'blood_group': u.blood_group, 'student_phone_num': u.student_phone_num, 'student_optional_phone_num': u.student_optional_phone_num,'father_name': u.father_name, 'mother_name': u.mother_name,'parent_email': u.parent_email, 'parent_phone_num': u.parent_phone_num,'parent_optional_phone_num': u.parent_optional_phone_num, 'permanent_address': u.permanent_address, 'permanent_address_zipcode': u.permanent_address_zipcode, 'local_guardian_name': u.local_guardian_name, 'local_guardian_address': u.local_guardian_name, 'local_guardian_address_zipcode': u.local_guardian_address_zipcode, 'local_guardian_phone_num': u.local_guardian_phone_num, 'local_guardian_optional_phone_num': u.local_guardian_optional_phone_num, 'local_guardian_email': u.local_guardian_email }
            if (u.distance_from_nsit != 0):
                return render(request,'student/students/studentProfile.html',data)    
            f = CreateStudentForm({'date_of_birth':u.date_of_birth, 'distance_from_nsit': u.distance_from_nsit, 'student_email': u.student_email, 'name':u.name, 'gender':u.gender, 'college_category':u.college_category, 'blood_group':u.blood_group, 'student_phone_num':u.student_phone_num, 'student_optional_phone_num':u.student_optional_phone_num, 'father_name':u.father_name, 'mother_name':u.mother_name, 'parent_email':u.parent_email, 'parent_phone_num':u.parent_phone_num, 'parent_optional_phone_num':u.parent_optional_phone_num, 'permanent_address':u.permanent_address, 'permanent_address_zipcode':u.permanent_address_zipcode, 'local_guardian_name':u.local_guardian_name, 'local_guardian_address':u.local_guardian_address, 'local_guardian_address_zipcode':u.local_guardian_address_zipcode, 'local_guardian_phone_num':u.local_guardian_phone_num, 'local_guardian_optional_phone_num':u.local_guardian_optional_phone_num, 'local_guardian_email':u.local_guardian_email })
            data = {'form': f,'all_hostels': b, 'username': student_id}
            return render(request, 'student/students/home.html',data)
    else:
        return redirect('logout')

# def studentProfile(request):
#     a=Hostels.objects.all();
#     b=[]
#     for i in a:
#         d={'name':i.hostel_name,'id':i.username}
#         b.append(d)
#     data = {'all_hostels': b,'student':'yes'}
#     return render(request,'student/students/home.html',data)
