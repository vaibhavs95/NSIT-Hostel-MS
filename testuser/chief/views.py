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
from .forms import *
@login_required
@require_http_methods(['GET', 'POST'])
def home(request):
    a=Hostels.objects.all();
    b=[]
    for i in a:
        d={'name':i.hostel_name,'id':i.username,'warden_name':i.name,'warden_nu':i.phone}
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
            fo = CreateWardenForm(request.POST or None)
            if fo.is_valid():
                user = MyUser.objects.create_user(fo.cleaned_data.get('userid'), '2016-02-02', fo.cleaned_data.get('password'))
                user.save()
                warden = Hostels(username = fo.cleaned_data.get('userid'))
                warden.chief_warden = ChiefWarden.objects.all()[0]
                hos = fo.cleaned_data.get('userid')
                f,m = hos.split('w')
                f,m=f.split('h')
                if f=='b':
                    warden.hostel_name = "Boys Hostel "+m
                elif f=='g':
                    warden.hostel_name= "Girls Hostel "+m
                warden.save()
                g = AddBranchForm()
                data = {'form': fo, 'userid': hos,'all_hostels': b,'branchform':g}
                return render(request, 'chief/add_hostel.html', data)
            else:
                g = AddBranchForm()
                data = {'form': fo, 'useridfail': fo.cleaned_data.get('userid'),'all_hostels': b,'branchform':g}
                return render(request, 'chief/add_hostel.html', data)
        else:
            fo = CreateWardenForm()
            g = AddBranchForm()
        data = {'form': fo,'all_hostels': b,'branchform':g}
        return render(request, 'chief/add_hostel.html',data)
    else:
        return redirect('logout')
@login_required
@require_http_methods(['GET', 'POST'])
def addbranch(request):
    if request.method == 'POST':
        fb = AddBranchForm(request.POST or None)
        if fb.is_valid():
            print(fb.cleaned_data.get('title'))
            b = Branch(title = fb.cleaned_data.get('title'),name = fb.cleaned_data.get('name'))
            b.save()
        g = CreateWardenForm()
        data = {'branchform': fb,'form':g}
        return render(request,'chief/add_hostel.html',data)
    else:
        g = CreateWardenForm()
        f = AddBranchForm()
        data = {'branchform': f,'form':g}
        return render(request,'chief/add_hostel.html',data)
@login_required
@require_http_methods(['GET', 'POST'])
def delete_hos(request):
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
#>>>>>>> 6f7c0af2dc6fb34ebfe38da446ca9d81fec8e224
