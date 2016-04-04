from django.shortcuts import render
from datetime import date
from reportlab.pdfgen import canvas
import re
from django.conf import settings
import base64, os
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
def MakeComplaint(request):
    alpha = str(request.user)
    if re.match('[0-9]*-[A-Z]*-[0-9]*',alpha) is not None:
        a=Hostels.objects.all();
        b=[]
        delta = Rooms.objects.get(students__username = alpha)
        delt = Hostels.objects.get(username = delta.hostel)
        mes = None
        for i in a:
            d={'name':i.hostel_name,'id':i.username}
            b.append(d)
        f = MakeComplaintForm(request.POST or None)
        if f.is_valid():
            a = f.save(commit = False)
            a.hostel = delt
            a.lodgers_roll_no = alpha
            a.save()
            mes = 'Complaint successfully lodged'
        s = Students.objects.get(username = alpha)
        comp = None
        try:
            comp = Complaints.objects.filter(hostel = delt,lodgers_roll_no = alpha)
        except ObjectDoesNotExist:
            pass
        data = {'form': f,'all_hostels': b,'comp':comp,'mes':mes,'stu':s}        
        return render(request, 'student/students/complaints.html',data)
    else:
        return redirect('logout')