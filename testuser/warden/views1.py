from django.shortcuts import render
import re, os,base64
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
from django.core.mail import send_mass_mail
from django.core.exceptions import ObjectDoesNotExist

def SendNoticeMail(title,usern):
    a = Students.objects.filter(room_number__hostel = usern )
    n = Notice.objects.get(title=title)
    url =  n.file.url
    url = "http://127.0.0.1:8000" + url
    c=[]
    message = "A new announcement has been put up by the Warden for all the residents of the hostel. Click <a href= '%s '>here </a> to view the announcement" % url
    for i in a:
       c.append(i.student_email)
    # email = EmailMessage()
    # email.subject = "New announcement for hostel residents of NSIT"
    # email.body = message
    # email.to = c
    # email.send()
    see = ("New announcement for hostel residents of NSIT",message,settings.EMAIL_HOST_USER,c)
    send_mass_mail((see,),fail_silently = True)
    return

@login_required
@require_http_methods(['GET', 'POST'])
def notices(request):
    if re.match("[bg]h[0-9]warden",str(request.user))!=None:
        mes = None
        if request.method =='POST':
            f=AddNoticeForm(request.POST,request.FILES)
            if f.is_valid():
                a = f.save(commit = False)
                a.creator = str(request.user)
                a.file = request.FILES['file']
                a.save();
                SendNoticeMail(f.cleaned_data.get('title'),str(request.user))
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
            a= Notice.objects.filter(creator= request.user)
        except ObjectDoesNotExist:
            pass
        data = {'all_hostels': b,'mes':mes,'form':f,'notices':a}
        return render(request,'warden/notices.html',data)
    else:
        return redirect('logout')
    
@login_required
@require_http_methods(['GET', 'POST'])
def delNotice(request,target):
    if re.match("[bg]h[0-9]warden",str(request.user))!=None:
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
        return redirect('warden-notices')
    else:
        return redirect('logout')
@login_required
@require_http_methods(['GET', 'POST'])
def remstudent(request,target):
    # pass
    if re.match("[bg]h[0-9]warden",str(request.user))!=None:
        mes  = None
        a = None
        b = None
        try:
            a = Students.objects.get(username = str(target))
        except ObjectDoesNotExist:
            pass # why pass ? if student is not there and there is request to remove that student,
            # then redirect to logout ?
            #return redirect('logout')
        try:
            b = Rooms.objects.get(students__username = str(target))
        except ObjectDoesNotExist:
            pass
        c = PreviousHostelDetail(hostel_name = b.hostel.hostel_name,room_no = b.room_no,student = a,hostel_join_date = a.current_hostel_join_date) # if not redirect to logout then there will be entry in previous hostel detail table with student = None.
        c.save()
        a.current_hostel_join_date = None
        a.room_number = None
        a.save()
        b.capacity_remaining = b.capacity_remaining+1
        b.save()
        mes = 'Student successfully removed'
        a=Hostels.objects.all();
        b=[]
        for i in a:
            d={'name':i.hostel_name,'id':i.username}
            b.append(d)
        u = Students.objects.get(username = target)
        prev = None
        crimi = None
        stu = Students.objects.get(username=target)
        try:
            prev = PreviousHostelDetail.objects.filter(student = stu)
        except ObjectDoesNotExist:
            pass
        try:
            crimi = CriminalRecord.objects.filter(student = stu)
        except ObjectDoesNotExist:
            pass
        data = {'all_hostels': b,'student':'yes', 'username': base64.b64encode(u.username.encode('utf-8')), 's': u,'prev':prev,'crim':crimi}
        # return render(request,'warden/studentProfile.html',data)
        return redirect("{% url 'WardenViewStudentProfile' u.username %}")
    else:
        return redirect('logout')

@login_required
def payfine(request,primkey,stu):
    if re.match("[bg]h[0-9]warden",str(request.user))!=None:
        delta = CriminalRecord.objects.get(pk = primkey)
        delta.paid = True
        delta.save()
        return redirect('WardenViewStudentProfile',student = stu)
    else:
        return redirect('logout')

@login_required
def StudentProfile(request,student):
    # pass
    if re.match("[bg]h[0-9]warden",str(request.user))!=None:
        a=Hostels.objects.all();
        b=[]
        for i in a:
            d={'name':i.hostel_name,'id':i.username}
            b.append(d)
        u = Students.objects.get(username = student)
        prev = None
        crimi = None
#        stu = Students.objects.get(username=student)
        try:
            prev = PreviousHostelDetail.objects.filter(student = u)
        except ObjectDoesNotExist:
            pass
        try:
            crimi = CriminalRecord.objects.filter(student = u).order_by('date_of_action')
        except ObjectDoesNotExist:
            pass
        data = {'all_hostels': b,'student':'yes','s': u,'prev':prev,'crim':crimi}
        return render(request,'warden/studentProfile.html',data)
    else:
        return redirect('logout')

@login_required
def ViewComplaint(request):
    if re.match("[bg]h[0-9]warden",str(request.user))!=None:
        a=Hostels.objects.all();
        b=[]
        for i in a:
            d={'name':i.hostel_name,'id':i.username}
            b.append(d)
        alpha = str(request.user)
        warden=Hostels.objects.get(username = alpha)
        comp = None
        try:
            comp = Complaints.objects.filter(hostel = warden,closed = False)
        except ObjectDoesNotExist:
            pass
        data = {'all_hostels': b,'comp':comp}
        return render(request,'warden/complaints.html',data)
    else:
        return redirect('logout')

@login_required
def CloseComplaint(request,target):
    if re.match("[bg]h[0-9]warden",str(request.user))!=None:
        alpha = str(request.user)
        target=int(target)
        warden=Hostels.objects.get(username = alpha)
        comp = None
        comp1 = Complaints.objects.filter(pk = target).update(closed=True)
        return redirect('wardenViewComplaint')
    else:
        return redirect('logout')
    
@login_required
@require_http_methods(['GET', 'POST'])
def detachStudent(request,target):
    h = Hostels.objects.get(username=request.user)
    try:
        rom = Rooms.objects.get(students__username = target)
    except ObjectDoesNotExist:
        return redirect('warden-student')
    s = Students.objects.get(username=target)
    a=Hostels.objects.all();
    b=[]
    for i in a:
        d={'name':i.hostel_name,'id':i.username}
        b.append(d)
    data = {}
    data['all_hostels'] = b
    crimi = None
    try:
        crimi = CriminalRecord.objects.filter(student = s)
        data['crimi'] = crimi
    except ObjectDoesNotExist:
        pass
    if re.match("[bg]h[0-9]+warden",str(request.user))!=None:
        if request.method == 'POST':
            f = DetachStudentForm(request.user, request.POST, instance = s)
            #searchedstudent = []
            if f.is_valid():
                rom.capacity_remaining+=1;
                s.room_number=None
                s.save()
                delta = PreviousHostelDetail(hostel_name = h.hostel_name,room_no = rom.room_no,student = s,hostel_join_date = s.current_hostel_join_date,
                    hostel_leave_date = f.cleaned_data.get('hostel_leave_date'))
                delta.save()
                rom.save()
                return redirect('warden-student')
            else:
                data['form'] = f
                return render(request,'warden/detachStudent.html',data)
        else:
            f = DetachStudentForm(request.user, instance = s)
            data['form'] = f
            return render(request, 'warden/detachStudent.html',data)
    else:
        return redirect('logout')

@login_required
@require_http_methods(['GET', 'POST'])
def addCriminalRecord(request,target):
    s = Students.objects.get(username = target)
    a=Hostels.objects.all();
    b=[]
    for i in a:
        d={'name':i.hostel_name,'id':i.username}
        b.append(d)
    data = {}
    data['all_hostels'] = b
    crimi = None
    if re.match("[bg]h[0-9]+warden",str(request.user))!=None:
        if request.method == 'POST':
            f = AddCriminalForm(request.POST,request.FILES)
            if f.is_valid():
                delta = f.save(commit = False)
                delta.student = s
                delta.file = request.FILES['file']
                delta.save()
                url = 'http://127.0.0.1:8000'+delta.file.url
                # subject_pa = 'NSIT-HMS Disciplinary action against your ward'
                # message_pa = '''Disciplinary actions have been taken against your ward for not following the code of conduct of the hostels properly.
                #     Refer to this <a href = '%s '> link </a> for more details.'''%(url)
                # subject = 'NSIT-HMS, Disciplinary action taken against you'
                # message = '''Disciplinary actions have been taken against you for not following the code of conduct of the hostels properly.
                #     Refer to this <a href = '%s '> link </a> for more details.'''%(url)
                # m1 = (subject_pa,message_pa,settings.EMAIL_HOST_USER,[s.parent_email,])
                # m2 = (subject,message,settings.EMAIL_HOST_USER,[s.student_email,])
                # send_mass_mail((m1,m2,),fail_silently = True)
                try:
                    crimi = CriminalRecord.objects.filter(student = target)
                    data['crimi'] = crimi
                except ObjectDoesNotExist:
                    pass
                data['stu'] = s.username
                data['form']=f
                return redirect('WardenViewStudentProfile', student=s.username)
            else:
                try:
                    crimi = CriminalRecord.objects.filter(student = target)
                    data['crimi'] = crimi
                except ObjectDoesNotExist:
                    pass
                data['stu'] = s.username
                data['form']=f
                return render(request,'warden/addDiscipline.html',data)
        else:
            f = AddCriminalForm()
            try:
                crimi = CriminalRecord.objects.filter(student = target)
                data['crimi'] = crimi
            except ObjectDoesNotExist:
                pass
            data['stu'] = s.username
            data['form']=f
            return render(request,'warden/addDiscipline.html',data)
    else:
        return redirect('logout')
@login_required
def viewDefaulters(request):
    alpha = str(request.user)
    if re.match("[bg]h[0-9]+warden",str(request.user))!=None:
        lis = HostelAttachDates.objects.filter(student__room_number__hostel__username=alpha,hostel_last_date__lt = date.today())
        count = len(lis)
        a=Hostels.objects.all();
        b=[]
        for i in a:
            d={'name':i.hostel_name,'id':i.username}
            b.append(d)
        data = {}
        data['all_hostels'] = b
        data['list'] = lis
        data['count'] = count
        return render(request,'warden/defaulterslist.html',data)
    else:
        return redirect('logout')
