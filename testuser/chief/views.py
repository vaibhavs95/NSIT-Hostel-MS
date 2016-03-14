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
    c = str(request.user)
    print(c == 'chiefwarden')
    if c =='chiefwarden':
        print (request)
        if request.method == 'POST':
            f = CreateWardenForm(request.POST or None)
            if f.is_valid():
                #print (f.userid)
                #print(f.cleaned_data.get('userid'))
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
                data = {'form': f, 'userid': hos}
                return render(request, 'newapp/chiefwarden/home.html', data)
            else:
                data = {'form': f, 'useridfail': f.cleaned_data.get('userid')}
                return render(request, 'newapp/chiefwarden/home.html', data)
        else:
            f = CreateWardenForm()
        data = {'form': f}
        return render(request, 'newapp/chiefwarden/home.html',data)
    else:
        return redirect('logout')
