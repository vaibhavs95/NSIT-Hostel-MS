from django.shortcuts import render
import re, os,base64
from django.shortcuts import render,redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from newapp.models import *
from .forms import *
from testuser import settings
from django.core.mail.message import EmailMessage
from django.core.exceptions import ObjectDoesNotExist

def SendNoticeMail(title,usern):
    a = Students.objects.filter( room_number__hostel = usern )
    print(a)
    n = Notice.objects.get(title=title)
    url =  n.file.url
    url = "http://127.0.0.1:8000" + url
    print(url)
    c=[]
    message = "A new announcement has been put up by the Chief Warden of NSIT for all the residents of the hostels. Click <a href= '%s'>here </a> to view the announcement" % url
    for i in a:
       c.append(i.student_email)
    email = EmailMessage()
    email.subject = "New announcement for hostel residents of NSIT"
    email.body = message
    email.to = c
    email.send()
    return

@login_required
@require_http_methods(['GET', 'POST'])
def notices(request):
    if re.match("[bg]h[0-9]warden",str(request.user))!=None:
        mes = None
        if request.method =='POST':
            f=AddNoticeForm(request.POST,request.FILES)
            if f.is_valid():
                a = f.save(commit = False)
                a.creator = str(request.user)
                a.file = request.FILES['file']
                a.save();
                SendNoticeMail(f.cleaned_data.get('title'),str(request.user))
                mes = 'Notice added successfully'
            else:
                f=AddNoticeForm()
        else:
            f=AddNoticeForm()
        a=Hostels.objects.all();
        b=[]
        for i in a:
            d={'name':i.hostel_name,'id':i.username}
            b.append(d)
        try:
            a= Notice.objects.filter(creator= request.user)
        except ObjectDoesNotExist:
            pass
        data = {'all_hostels': b,'mes':mes,'form':f,'notices':a}
        return render(request,'warden/notices.html',data)
    else:
        return redirect('logout')
    
@login_required
@require_http_methods(['GET', 'POST'])
def delNotice(request,target):
    if re.match("[bg]h[0-9]warden",str(request.user))!=None:
        mes  = None
        f= AddNoticeForm()
        try:
            c=Notice.objects.get(pk=target)
        except ObjectDoesNotExist:
            pass
        url =  c.file.url
        delta = settings.MEDIA_ROOT
        delta = delta.split('media')[-2]
        url = delta+url
        os.remove(url)
        c.delete()
        mes  = 'Notice removed succeessfully'
        a=Hostels.objects.all();
        b=[]
        for i in a:
            d={'name':i.hostel_name,'id':i.username}
            b.append(d)
        try:
            a= Notice.objects.filter(creator= request.user)
        except ObjectDoesNotExist:
            pass
        data = {'all_hostels': b,'mes':mes,'form':f,'notices':a}
        return render(request,'warden/notices.html',data)
    else:
        return redirect('logout')
@login_required
@require_http_methods(['GET', 'POST'])
def remstudent(request,target):
    # pass
    if re.match("[bg]h[0-9]warden",str(request.user))!=None:
        mes  = None
        a = None
        b = None
        try:
            a = Students.objects.get(username = str(target))
        except ObjectDoesNotExist:
            pass
        
        try:
            b = Rooms.objects.get(students__username = str(target))
        except ObjectDoesNotExist:
            pass
        c = PreviousHostelDetail(hostel_name = b.hostel.hostel_name,room_no = b.room_no,student = a,hostel_join_date = a.current_hostel_join_date)
        c.save()
        a.current_hostel_join_date = None
        a.room_number = None
        a.save()
        b.capacity_remaining = b.capacity_remaining+1
        b.save()
        mes = 'Student successfully removed'
        a=Hostels.objects.all();
        b=[]
        for i in a:
            d={'name':i.hostel_name,'id':i.username}
            b.append(d)
        u = Students.objects.get(username = target)
        prev = None
        crimi = None
        try:
            prev = PreviousHostelDetail.objects.filter(student = target)
        except ObjectDoesNotExist:
            pass
        try:
            crimi = CriminalRecord.objects.filter(student = target)
        except ObjectDoesNotExist:
            pass
        data = {'all_hostels': b,'student':'yes', 'username': base64.b64encode(u.username.encode('utf-8')), 's': u,'prev':prev,'crim':crimi}
        return render(request,'warden/studentProfile.html',data)
    else:
        return redirect('logout')
    
def payfine(request,primkey,stu):
    if re.match("[bg]h[0-9]warden",str(request.user))!=None:
        delta = CriminalRecord.objects.get(pk = primkey)
        delta.paid_or_not = True
        delta.save()
        a=Hostels.objects.all();
        b=[]
        for i in a:
            d={'name':i.hostel_name,'id':i.username}
            b.append(d)
        u = Students.objects.get(username = alpha)
        prev = None
        crimi = None
        try:
            prev = PreviPreviousHostelDetail.objects.filter(student = stu)
        except ObjectDoesNotExist:
            pass
        try:
            crimi = CriminalRecord.objects.filter(student = stu)
        except ObjectDoesNotExist:
            pass
        mes = 'Fine Payed successfully'
        data = {'all_hostels': b,'student':'yes', 'username': student_id, 's': u,'prev':prev,'crim':crimi,'mes':mes}
        return render(request,'warden/studentProfile.html',data)
    else:
        return redirect('logout')
    
def StudentProfile(request,student):
    # pass
    if re.match("[bg]h[0-9]warden",str(request.user))!=None:
        a=Hostels.objects.all();
        b=[]
        for i in a:
            d={'name':i.hostel_name,'id':i.username}
            b.append(d)
        print(student)
        u = Students.objects.get(username = student)
        prev = None
        crimi = None
        try:
            prev = PreviousHostelDetail.objects.filter(student = student)
        except ObjectDoesNotExist:
            pass
        try:
            crimi = CriminalRecord.objects.filter(student = student)
        except ObjectDoesNotExist:
            pass
        data = {'all_hostels': b,'student':'yes', 'username': base64.b64encode(u.username.encode('utf-8')), 's': u,'prev':prev,'crim':crimi}
        return render(request,'warden/studentProfile.html',data)
    else:
        return redirect('logout')

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
