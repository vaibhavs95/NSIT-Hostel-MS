import re
import base64
from django.shortcuts import render,redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mass_mail
from .models import *
from .forms import *
from testuser import settings

@require_http_methods(['GET', 'POST'])
def base(request):
    f = LoginForm(request.POST or None)
    if f.is_valid():
        return redirect('login')
    else:
        f=LoginForm()
    hos=Hostels.objects.all().order_by('hostel_name')
    next_url = request.GET.get('next')
    noti = None
    try:
        noti = Notice.objects.filter(creator = 'chiefwarden').order_by('-pk')
    except ObjectDoesNotExist:
        pass
    data = { 'next' : next_url, 'form': f,'hostels':hos,'len':len(hos),'noti':noti}
    return render(request, 'newapp/base.html', data);

@require_http_methods(['GET', 'POST'])
def handleLogin(request):
    if request.user.is_authenticated():
        return redirect('home')
    f = LoginForm(request.POST or None)
    forgot = ForgetForm(request.POST or None)
    if request.method=='POST':
        nexturl = request.POST.get('next')
    if f.is_valid():
        user = f.get_user();
        login(request, user);
        if re.match("chief[a-zA-Z0-9_]*",str(user))!=None:
            a = ChiefWarden.objects.get(username = user)
            data = {'next' : nexturl, 'name': a.name}
            return redirect('chiefwarden-home')
        elif re.match("[a-zA-Z0-9_]*warden",str(user))!=None:
            a = Hostels.objects.get(username = user)
            data = {'next' : nexturl, 'name': a.username}
            return redirect('warden-home')
        elif re.match("[0-9]*-[A-Za-z0-9]*",str(user))!=None:
            a = Students.objects.get(username = user)
            alpha = str(base64.b64encode(a.username.encode('utf-8')).decode('utf-8'))
            data = {'next' : nexturl, 'username': alpha}
            return redirect('studentid', student_id = alpha)
        else:
            return redirect('logout')
    mes = None
    if forgot.is_valid():
        userid = forgot.cleaned_data.get('UserId')
        subject = 'NSIT- Hostel Managemant ystem Reset Password'
        messa = 'http://127.0.0.1:8000/newapp/resetpassword/'+str(base64.b64encode(userid.encode('utf-8')).decode('utf-8'))
        message = "Please Click on this link <a href='%s ' to reset your password"%(messa)
        if re.match("chief[a-zA-Z0-9_]*",str(userid))!=None:
            try:
                a = ChiefWarden.objects.get(username = userid)
                m1 = (subject,message,settings.EMAIL_HOST_USER,[a.email])
                send_mass_mail((m1,),fail_silently = False)
            except ObjectDoesNotExist:
                pass
        elif re.match("[a-zA-Z0-9_]*warden",str(userid))!=None:
            try:
                a = Hostels.objects.get(username = userid)
                m1 = (subject,message,settings.EMAIL_HOST_USER,[a.email])
                send_mass_mail((m1,),fail_silently = False)
            except ObjectDoesNotExist:
                pass
        elif re.match("[0-9]*-[A-Za-z0-9]*",str(userid))!=None:
            try:
                a = Students.objects.get(username = userid)
                m1 = (subject,message,settings.EMAIL_HOST_USER,[a.student_email])
                send_mass_mail((m1,),fail_silently = False)
            except ObjectDoesNotExist:
                pass
        mes = 'A verification mail has been sent to your registered mail, if userid was valid'
    a=Hostels.objects.all();
    b=[]
    for i in a:
        d={'name':i.hostel_name,'id':i.username}
        b.append(d)
    data = {'all_hostels': b,'form':f,'forgetform':forgot,'mes':mes}
    return render(request,'newapp/login.html',data)

@require_GET    
@login_required
def home(request):
    a=request.user
    if re.match("AnonymousUser",str(a))!=None:
        return redirect('base')
    elif re.match("chief[a-zA-Z0-9_]*",str(a))!=None:
        return redirect('chiefwarden-home')
    elif re.match("[a-zA-Z0-9_]*warden",str(a))!=None:
        return redirect('warden-home')
    else:
        a = Students.objects.get(username = a)
        alpha = str(base64.b64encode(a.username.encode('utf-8')).decode('utf-8'))
        #data = {'next' : nexturl, 'username': alpha}
        return redirect('studentid', student_id = alpha)

@require_GET
def logoutview(request):
    logout(request)
    return redirect('base')

@require_http_methods(['GET', 'POST'])
def hostels(request,hostel_name):
    if request.method=='POST':
        f = LoginForm(request.POST or None)
        if f.is_valid():
            return redirect('login')
    else:
        f=LoginForm()
    a=Hostels.objects.all();
    b=[]
    for i in a:
        d={'name':i.hostel_name,'id':i.username}
        b.append(d)
        if i.username == hostel_name:
            c = i
    faci = None
    try:
        faci = Facilities.objects.filter(hostel = hostel_name)
    except ObjectDoesNotExist:
        pass
    council = None
    try:
        council = HostelCouncil.objects.filter(hostel = hostel_name)
    except ObjectDoesNotExist:
        pass
    mess =None
    try:
        mess = MessDetail.objects.get(hostel = hostel_name)
    except ObjectDoesNotExist:
        pass
    data = {'all_hostels': b,'target_hostel':c,'form':f,'faci':faci,'council':council,'mess':mess}
    return render(request,'newapp/bh1_facilities.html',data)

@require_http_methods(['GET', 'POST'])
def resetPassword(request,target):
    alpha = str(base64.b64decode(target))
    alpha = alpha[2:-1]
    f = ResetPasswordForm(request.POST or None)
    mes = None
    if f.is_valid():
        pas = f.cleaned_data.get('new_Password')
        try:
            b = MyUser.objects.get(userid = alpha)
            b.set_password(pas)
            b.save()
            mes = 'Password reset successful'
        except ObjectDoesNotExist:
            pass
    a=Hostels.objects.all();
    b=[]
    for i in a:
        d={'name':i.hostel_name,'id':i.username}
        b.append(d)
    data = {'all_hostels': b,'form':f,'mes':mes}
    return render(request,'newapp/resetPassword.html',data)
    