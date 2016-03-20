from django.shortcuts import render
import re

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
def home(request):
    a=Hostels.objects.all();
    b=[]
    for i in a:
        d={'name':i.hostel_name,'id':i.username,'warden_name':i.warden_name,'warden_nu':i.warden_phone_num}
        b.append(d)
    alpha = str(request.user)
    if alpha =='chiefwarden':
        data = {'all_hostels': b}
        return render(request, 'chief/home.html',data)
    else:
        return redirect('logout')
@login_required
@require_http_methods(['GET', 'POST'])
def add_hos(request):
    a=Hostels.objects.all();
    b=[]
    for i in a:
        d={'name':i.hostel_name,'id':i.username}
        b.append(d)
    alpha = str(request.user)
    if alpha =='chiefwarden':
        if request.method == 'POST':
            f = CreateWardenForm(request.POST or None)
            if f.is_valid():
                user = MyUser.objects.create_user(f.cleaned_data.get('userid'), '2016-02-02', f.cleaned_data.get('password'))
                user.save()
                warden = Hostels(username = f.cleaned_data.get('userid'))
                warden.chief_warden = ChiefWarden.objects.all()[0]
                hos = f.cleaned_data.get('userid')
                f,m = hos.split('w')
                f,m=f.split('h')
                if f=='b':
                    warden.hostel_name = "Boys Hostel "+m
                elif f=='g':
                    warden.hostel_name= "Girls Hostel "+m
                warden.save()
                g = CreateWardenForm()
                data = {'form': g, 'userid': hos,'all_hostels': b}
                return render(request, 'chief/add_hostel.html', data)
            else:
                data = {'form': f, 'useridfail': f.cleaned_data.get('userid'),'all_hostels': b}
                return render(request, 'chief/add_hostel.html', data)
        else:
            f = CreateWardenForm()
        data = {'form': f,'all_hostels': b}
        return render(request, 'chief/add_hostel.html',data)
    else:
        return redirect('logout')

@login_required
@require_http_methods(['GET', 'POST'])
def delete_hos(request,target):
    a=Hostels.objects.all();
    b=[]
    for i in a:
        d={'name':i.hostel_name,'id':i.username}
        b.append(d)
    alpha = str(request.user)
    if alpha =='chiefwarden':
        try:
            a=Rooms.objects.filter(hostel = target)
        except ObjectDoesNotExist:
            pass
        for i in a:
            if i.filled_rooms != 0:             
                messages.warning(request, 'Your account expires in three days.')
        data = {'all_hostels': b}
        return render(request, 'chief/home.html',data)
    else:
        return redirect('logout')