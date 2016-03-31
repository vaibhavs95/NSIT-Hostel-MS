import re
import base64
from django.shortcuts import render,redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import *
from .forms import LoginForm

@require_http_methods(['GET', 'POST'])
def base(request):
    if request.method=='POST':
        f = LoginForm(request.POST or None)
        if f.is_valid():
            return redirect('login')
    else:
        f=LoginForm()
    hos=Hostels.objects.all().order_by('hostel_name')
    next_url = request.GET.get('next')
    data = { 'next' : next_url, 'form': f,'hostels':hos,'len':len(hos)}
    return render(request, 'newapp/base.html', data);

@require_http_methods(['GET', 'POST'])
def handleLogin(request):
    if request.user.is_authenticated():
        return redirect('home')
    f = LoginForm(request.POST or None)
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
    a=Hostels.objects.all();
    b=[]
    for i in a:
        d={'name':i.hostel_name,'id':i.username}
        b.append(d)
    data = {'all_hostels': b,'form':f}
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
    data = {'all_hostels': b,'target_hostel':c,'form':f}
    return render(request,'newapp/bh1_facilities.html',data)