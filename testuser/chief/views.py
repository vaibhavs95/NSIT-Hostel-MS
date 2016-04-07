from django.shortcuts import render
import re, os
import base64
from django.shortcuts import render,redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from newapp.models import *
from .forms import *
from warden.forms import SearchStudentRollNoForm, SearchStudentOtherForm
from testuser import settings
from django.core.mail import send_mass_mail
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
            return redirect('chiefwarden-home')
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
    url = "http://127.0.0.1:8000" + url
    c=[]
    message = "A new announcement has been put up by the Chief Warden of NSIT for all the residents of the hostels. Click <a href= '%s '>here </a> to view the announcement" % url
    for i in a:
       c.append(i.student_email)
    # email = EmailMessage()
    # email.subject = "New announcement for hostel residents of NSIT"
    # email.body = message
    # email.to = c
    # email.send()
    see = ("New announcement for hostel residents of NSIT",message,settings.EMAIL_HOST_USER,c)
    send_mass_mail((see,),fail_silently = False)
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
        return redirect('chiefwarden-notices')
    else:
        return redirect('logout')
    
def StudentProfile(request,student):
    # pass
    alpha = request.user
    if alpha == 'chiefwarden':
        a=Hostels.objects.all();
        b=[]
        for i in a:
            d={'name':i.hostel_name,'id':i.username}
            b.append(d)
        u = Students.objects.get(username = student)
        prev = None
        crimi = None
        try:
            prev = PreviPreviousHostelDetail.objects.filter(student = student)
        except ObjectDoesNotExist:
            pass
        try:
            crimi = CriminalRecord.objects.filter(student = student)
        except ObjectDoesNotExist:
            pass
        data = {'all_hostels': b,'student':'yes', 'username': student_id, 's': u,'prev':prev,'crim':crimi}
        return render(request,'chief/studentProfile.html',data)
    else:
        return redirect('logout')


data = {}

def basic():
    data.clear()
    a = Hostels.objects.all();
    b = []
    for i in a:
        d = {'name': i.hostel_name, 'id': i.username}
        b.append(d)
    data['all_hostels'] = b

def studentbasic(user):
    g = SearchStudentRollNoForm()
    data['searchstudentrollnoform'] = g
    h = SearchStudentOtherForm()
    data['searchstudentotherform'] = h
    data['searchedstudent'] = None
    data['searchedstudentnotfound'] = None
    return

@login_required
@require_http_methods(['GET', 'POST'])
def student(request):
    if re.match("chiefwarden", str(request.user)) != None:
        basic()
        studentbasic(request.user)
        return render(request, 'chief/student.html', data)
    else:
        return redirect('logout')

@login_required
@require_http_methods(['GET', 'POST'])
def searchstudentrollno(request):
    if re.match("chiefwarden", str(request.user)) != None:
        basic()
        studentbasic(str(request.user))
        searchedstudent = []
        p = None
        if request.method == 'POST':
            f = SearchStudentRollNoForm(request.POST or None)
            if f.is_valid():
                roll_no = f.cleaned_data.get('roll_no')
                try:
                   sx = Students.objects.get(username=roll_no)
                except ObjectDoesNotExist:
                    data['searchedstudentnotfound'] = 'yes'
                if not data['searchedstudentnotfound']:
                    if sx.room_number:
                        p = {'username':sx.username, 'id':base64.b64encode(sx.username.encode('utf-8'))}
                    else:
                        p = {'username':sx.username, 'id':base64.b64encode(sx.username.encode('utf-8')),'freestudent':'yes'}
                    if p:
                        searchedstudent.append(p)
                data['searchedstudent'] = searchedstudent
                data['searchstudentrollnoform'] = f
                return render(request,'chief/student.html',data)
            else:
                data['searchstudentrollnoform'] = f
                return render(request,'chief/student.html',data)
        else:
            return render(request, 'chief/student.html',data)
    else:
        return redirect('logout')


@login_required
@require_http_methods(['GET', 'POST'])
def searchstudentother(request):
    if re.match("chiefwarden",str(request.user))!=None:
        basic()
        studentbasic(str(request.user))
        searchedstudent = []
        if request.method == 'POST':
            f = SearchStudentOtherForm(request.POST or None)
            if f.is_valid():
                name = None
                date_of_birth = None
                sx = []
                name = f.cleaned_data.get('name')
                date_of_birth = f.cleaned_data.get('date_of_birth')
                if name and date_of_birth:
                    try:
                        sx = Students.objects.filter(name__icontains = name, date_of_birth = date_of_birth)
                    except ObjectDoesNotExist:
                        data['searchedstudentnotfound'] = 'yes'
                elif name and not date_of_birth:
                    try:
                        sx = Students.objects.filter(name__icontains = name)
                    except ObjectDoesNotExist:
                        data['searchedstudentnotfound'] = 'yes'
                elif not name and date_of_birth:
                    try:
                        sx = Students.objects.filter(date_of_birth = date_of_birth)
                    except ObjectDoesNotExist:
                        data['searchedstudentnotfound'] = 'yes'
                if(len(sx) < 1):
                    data['searchedstudentnotfound'] = 'yes'
                if not data['searchedstudentnotfound']:
                    for i in sx:
                        p = None
                        if i.room_number:
                            p = {'username':i.username, 'id':base64.b64encode(i.username.encode('utf-8'))}
                        else:
                            p = {'username':i.username, 'id':base64.b64encode(i.username.encode('utf-8')),'freestudent':'yes'}
                        if p:
                            searchedstudent.append(p)
                data['searchedstudent'] = searchedstudent
                data['searchstudentotherform'] = f
                return render(request,'chief/student.html',data)
            else:
                data['searchstudentotherform'] = f
                return render(request,'chief/student.html',data)
        else:
            return render(request, 'chief/student.html',data)
    else:
        return redirect('logout')


def roombasic():
    #basic()
    data['studentnotinroom'] = None
    data['studentinroom'] = None
    data['searchedroom'] = None
    data['searchedroomnotfound'] = None
    g = SearchHostelRoomForm()
    data['searchroomform'] = g
    return

@login_required
@require_http_methods(['GET', 'POST'])
def room(request):
    if re.match("chiefwarden", str(request.user)) != None:
        basic()
        roombasic()
        return render(request, 'chief/room.html', data)
    else:
        return redirect('logout')

@login_required
@require_http_methods(['GET', 'POST'])
def searchroom(request):
    if re.match("chiefwarden", str(request.user)) != None:
        basic()
        roombasic()
        if request.method == 'POST':
            f = SearchHostelRoomForm(request.POST)
            if f.is_valid():
                hostel = f.cleaned_data.get('hostel')
#                h = Hostels.objects.get(username=hostel)
                room_no = f.cleaned_data.get('room_no')
                room_no = room_no.upper()
                a = None
                try:
                    a = Rooms.objects.get(hostel=hostel, room_no=room_no)
                except ObjectDoesNotExist:
                    data['searchedroomnotfound'] = 'yes'
                if not data['searchedroomnotfound']:
                    s = None
                    try:
                        s = Students.objects.filter(room_number=a)
                    except ObjectDoesNotExist:
                        pass
                    student = []
                    for j in s:
                        p = {'username': j.username, 'id': base64.b64encode(
                            j.username.encode('utf-8'))}
                        student.append(p)
                    d = {'room': a, 'students': student}
                    data['searchedroom'] = d
                data['searchroomform'] = f
                return render(request, 'chief/room.html', data)
            else:
                data['searchroomform'] = f
                return render(request, 'chief/room.html', data)
        else:
            f = SearchHostelRoomForm()
            data['searchroomform'] = f
            return render(request, 'chief/room.html', data)
    else:
        return redirect('logout')

def addBank(request):
    if str(request.user) == 'chiefwarden':
        f = addBankForm(request.POST or None)
        mes = None
        if f.is_valid():
            kent = f.save(commit=False)
            kent.name = kent.name.upper()
            kent.save()
            mes = 'Bank added successfully'
        a=Hostels.objects.all();
        b=[]
        for i in a:
            d={'name':i.hostel_name,'id':i.username,'warden_name':i.name,'warden_nu':i.phone}
            b.append(d)
        delta = Banks.objects.all()
        data = {'all_hostels': b,'form':f,'banks':delta}
        return render(request, 'chief/addBank.html',data)
    else:
        return redirect('logout')