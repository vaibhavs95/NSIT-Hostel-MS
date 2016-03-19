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
def createWarden(request):
    a=Hostels.objects.all();
    b=[]
    for i in a:
        d={'name':i.hostel_name,'id':i.username}
        b.append(d)
    alpha = str(request.user)
    if alpha =='chiefwarden':
        print (request)
        if request.method == 'POST':
            fo = CreateWardenForm(request.POST or None)
            if fo.is_valid():
                #print (f.userid)
                #print(f.cleaned_data.get('userid'))
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
                return render(request, 'chief/chiefwarden/home.html', data)
            else:
                g = AddBranchForm()
                data = {'form': fo, 'useridfail': fo.cleaned_data.get('userid'),'all_hostels': b,'branchform':g}
                return render(request, 'chief/chiefwarden/home.html', data)
        else:
            fo = CreateWardenForm()
            g = AddBranchForm()
        data = {'form': fo,'all_hostels': b,'branchform':g}
        return render(request, 'chief/chiefwarden/home.html',data)
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
        return render(request,'chief/chiefwarden/home.html',data)
    else:
        g = CreateWardenForm()
        f = AddBranchForm()
        data = {'branchform': f,'form':g}
        return render(request,'chief/chiefwarden/home.html',data)