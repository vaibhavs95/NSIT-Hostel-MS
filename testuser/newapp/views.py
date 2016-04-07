import re
import base64,random,string
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
        if re.match("chief[a-z]*",str(user))!=None:
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
        pas = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(10))
        subject = 'NSIT- Hostel Managemant ystem Reset Password'
        message = """Following is your new temporary password, use this to login into NSIT-HMS and do reset your password once you login.
        UserId: %s,
        Password: %s"""%(userid,pas)
        if userid=='chiefwarden':
            try:
                a = ChiefWarden.objects.get(username = userid)
                b = MyUser.objects.get(userid=userid)
                b.set_password(pas)
                b.save()
                m1 = (subject,message,settings.EMAIL_HOST_USER,[a.email])
                send_mass_mail((m1,),fail_silently = False)
            except ObjectDoesNotExist:
                pass
        elif re.match("[a-zA-Z0-9_]*warden",str(userid))!=None:
            try:
                a = Hostels.objects.get(username = userid)
                b = MyUser.objects.get(userid=userid)
                b.set_password(pas)
                b.save()
                m1 = (subject,message,settings.EMAIL_HOST_USER,[a.email])
                send_mass_mail((m1,),fail_silently = False)
            except ObjectDoesNotExist:
                pass
        elif re.match("[0-9]*-[A-Za-z0-9]*",str(userid))!=None:
            try:
                a = Students.objects.get(username = userid)
                b = MyUser.objects.get(userid=userid)
                b.set_password(pas)
                b.save()
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

def capacityremaining(user):
    user = Hostels.objects.get(username=user)
    r = Rooms.objects.filter(hostel=user, capacity_remaining__gt=0)
    v = 0
    for i in r:
        v = v + i.capacity_remaining
    return v


def capacity(user):
    h = Hostels.objects.get(username=user)
    r = Rooms.objects.filter(hostel=h)
    v = 0
    for i in r:
        v = v + i.capacity_of_room
    return v

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
    c=None
    for i in a:
        d={'name':i.hostel_name,'id':i.username}
        b.append(d)
        if i.username == hostel_name:
            c = i
    data = {'all_hostels': b,'target_hostel':c,'form':f}
    
    h = Hostels.objects.get(username = hostel_name)
    a = Facilities.objects.filter(hostel = h)
    facilities = []
    for i in a:
        if i.photo:
            d = {'fac': i, 'photo': 'yes'}
        else:
            d = {'fac': i, 'photo': None}
        facilities.append(d)
    data['facilities'] = facilities
        #data['name'] = user.name
        #data['phone'] = user.phone
        #data['landline'] = user.landline
        #data['email'] = user.email
        #data['dept'] = user.department
        #data['portfolio'] = user.portfolio
    data['total_rooms'] = capacity(h.username)
    data['rooms_available'] = capacityremaining(h.username)
    if h.warden_photo:
        data['wardenphoto'] = 'yes'
        data['userid'] = h
    else:
        data['wardenphoto'] = None
        data['userid'] = None
    hc = HostelCouncil.objects.filter(hostel=h)
    council = []
    for i in hc:
        if i.photo:
            d = {'coun': i, 'photo': 'yes'}
        else:
            d = {'coun': i, 'photo': None}
        council.append(d)
    data['council'] = council
    hf = (Form.objects.filter(hostel=h)).order_by('time')
    hosform = []
    for i in hf:
        d = {'hosf': i}
        hosform.append(d)
    data['hosform'] = hosform
    messdetail = MessDetail.objects.filter(hostel=h)
    if messdetail:
        data['mess'] = messdetail[0]
    else:
        data['mess'] = None
    return render(request,'newapp/bh1_facilities.html',data)

@require_http_methods(['GET', 'POST'])
def resetPassword(request):
    if request.user.is_authenticated():
        f = ResetPasswordForm(request.POST or None)
        mes = None
        if f.is_valid():
            pas = f.cleaned_data.get('new_Password')
            try:
                b = MyUser.objects.get(userid = str(request.user))
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
    else:
        return redirect('logout')
    