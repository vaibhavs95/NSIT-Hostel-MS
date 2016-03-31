from django.shortcuts import render
import re, os
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
@login_required
@require_http_methods(['GET', 'POST'])
def home(request):
    alpha = str(request.user)
    if alpha =='chiefwarden':
        f = CreateWardenForm(request.POST or None)
        if f.is_valid():
            user = MyUser.objects.create_user(f.cleaned_data.get('userid'), '2016-02-02', f.cleaned_data.get('password'))
            user.save()
            warden = Hostels(username = f.cleaned_data.get('userid'))
            warden.chief_warden = ChiefWarden.objects.all()[0]
            hos = str(f.cleaned_data.get('userid'))
            fo,m = hos.split('w')
            fo,m = fo.split('h')
            if fo=='b':
                warden.hostel_name = "Boys Hostel "+m
            elif fo=='g':
                warden.hostel_name= "Girls Hostel "+m
            warden.save()
        a=Hostels.objects.all();
        b=[]
        for i in a:
            d={'name':i.hostel_name,'id':i.username,'warden_name':i.name,'warden_nu':i.phone}
            b.append(d)
        data = {'all_hostels': b,'form':f}
        return render(request, 'chief/home.html',data)
    else:
        return redirect('logout')

@login_required
@require_http_methods(['GET', 'POST'])
def addbranch(request):
    alpha = str(request.user)
    if alpha =='chiefwarden':
        fb = AddBranchForm(request.POST or None)
        mes = None
        if fb.is_valid():
            b = Branch(title = fb.cleaned_data.get('title'),name = fb.cleaned_data.get('name'),roll_code=fb.cleaned_data.get('Roll_Code'))
            b.save()
            mes = 'Branch added successfully.'
        a=Hostels.objects.all();
        b=[]
        for i in a:
            d={'name':i.hostel_name,'id':i.username,'warden_name':i.name,'warden_nu':i.phone}
            b.append(d)
        a= Branch.objects.all()
        data = {'all_branch':a,'form':fb,'mes':mes,'all_hostels':b}        
        return render(request,'chief/branches.html',data)
    else:
        return redirect('logout')

@login_required
@require_http_methods(['GET', 'POST'])
def delete_hos(request,target):
    alpha = str(request.user)
    if alpha =='chiefwarden':
        try:
            a=Rooms.objects.filter(hostel = target)
        except ObjectDoesNotExist:
            pass
        j=0
        mes = None
        for i in a:
            if i.capacity_remaining != i.capacity_of_room:
                mes="Hostel still has some rooms alloted and thus can't be deleted."
                j=1
                break
        if j==0 :
            a.delete()
            try:
                a = Hostels.objects.filter(username = target)
            except ObjectDoesNotExist:
                pass
            a.delete()
            try:
                a = MyUser.objects.get(userid = target)
            except ObjectDoesNotExist:
                pass
            a.delete()
            mes="Hostel deleted successfully."
        f=CreateWardenForm(request.POST or None)
        if f.is_valid():
            user = MyUser.objects.create_user(f.cleaned_data.get('userid'), '2016-02-02', f.cleaned_data.get('password'))
            user.save()
            warden = Hostels(username = f.cleaned_data.get('userid'))
            warden.chief_warden = ChiefWarden.objects.all()[0]
            hos = f.cleaned_data.get('userid')
            fo,m = str(hos.split('w'))
            fo,m=f.split('h')
            if fo=='b':
                warden.hostel_name = "Boys Hostel "+m
            elif fo=='g':
                warden.hostel_name= "Girls Hostel "+m
            warden.save()
        a=Hostels.objects.all();
        b=[]
        for i in a:
            d={'name':i.hostel_name,'id':i.username}
            b.append(d)
        data = {'all_hostels': b,'mes':mes,'form':f}
        return render(request, 'chief/home.html',data)
    else:
        return redirect('logout')

def SendNoticeMail(fileAddress,title):
    a = Students.objects.exclude( room_number = None)
    n = Notice.objects.get(title=title)
    url =  n.file.url
    url = "127.0.0.1:8000" + url
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
    alpha = str(request.user)
    if alpha =='chiefwarden':
        mes = None
        if request.method =='POST':
            f=AddNoticeForm(request.POST,request.FILES)
            if f.is_valid():
                a = f.save(commit = False)
                a.creator = 'chiefwarden'
                a.file = request.FILES['file']
                a.save();
                SendNoticeMail(request.FILES['file'].name,f.cleaned_data.get('title'))
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
            a= Notice.objects.filter(creator= 'chiefwarden')
        except ObjectDoesNotExist:
            pass
        data = {'all_hostels': b,'mes':mes,'form':f,'notices':a}
        return render(request,'chief/notices.html',data)
    else:
        return redirect('logout')
    
@login_required
@require_http_methods(['GET', 'POST'])
def delNotice(request,target):
    alpha = str(request.user)
    if alpha =='chiefwarden':
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
            a= Notice.objects.filter(creator= 'chiefwarden')
        except ObjectDoesNotExist:
            pass
        data = {'all_hostels': b,'mes':mes,'form':f,'notices':a}
        return render(request,'chief/notices.html',data)
    else:
        return redirect('logout')