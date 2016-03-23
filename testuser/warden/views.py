import re, os, base64

from django.shortcuts import render,redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.core.mail import EmailMessage
from django.conf import settings
from newapp.models import *
from newapp.forms import *
from .forms import *


data = {}
def basic():
	a = Hostels.objects.all();
	b = []
	for i in a:
		d = {'name':i.hostel_name,'id':i.username}
		b.append(d)
	data['all_hostels'] = b
@require_http_methods(['GET', 'POST'])
@login_required
def home(request):
	if re.match("[bg]h[0-9]warden",str(request.user))!=None:
		user = Hostels.objects.get(username=request.user)
		data['name'] = user.name
		data['phone'] = user.phone
		data['landline'] = user.landline
		data['email'] = user.email
		data['dept'] = user.department
		data['portfolio'] = user.portfolio
		data['total_rooms'] = len(Rooms.objects.filter(hostel=user))
		data['rooms_available'] = len(Rooms.objects.filter(hostel=user,capacity_remaining__gt = 0))
		data['rooms_filled'] = len(Rooms.objects.filter(hostel=user,capacity_remaining = 0))
		if user.warden_photo:
			data['userid'] = user
		else:
			data['userid'] = None
		basic()
		f = EditWardenProfileForm(request = request,instance = user)
		data['editprofileform']=f
		return render(request,'warden/home.html',data)
	else:
		return redirect('logout')
@require_http_methods(['GET', 'POST'])
@login_required
def profileedit(request):
	if re.match("[bg]h[0-9]warden",str(request.user))!=None:
		basic()
		h = Hostels.objects.get(username=request.user)
		if request.method == 'POST':
			a = None
			a = request.FILES.__contains__('warden_photo')
			if a:
				h.warden_photo.delete(True)
			f = EditWardenProfileForm(request.POST, request.FILES, request=request, instance = h)
			if f.is_valid():
				f.save()
				g = EditWardenProfileForm(request = request,instance = h)
				data['editprofileform'] = g
				data['userid'] = h
				return redirect('warden-home')
			else:
				data['editprofileform'] = f
				data['userid'] = h
				return render(request,'warden/home.html',data)
		else:
			f = EditWardenProfileForm(request = request,instance = h)
			data['userid'] = h
			data['editprofileform']=f
			return render(request,'warden/home.html',data)
	else:
		return redirect('logout')
@login_required
@require_http_methods(['GET', 'POST'])
def room(request):
	if re.match("[bg]h[0-9]warden",str(request.user))!=None:
		basic()
		h = Hostels.objects.get(username = request.user)
		a = (Rooms.objects.filter(hostel=h)).order_by('room_no')
		rooms = []
		for i in a:
			d = {'room_no':i.room_no,'capacity':i.capacity_of_room,'capacity_remaining':i.capacity_remaining}
			rooms.append(d)
		data['rooms'] = rooms
		f = AddRoomForm()
		data['addroomform'] = f
		return render(request,'warden/room.html',data)
	else:
		return redirect('logout')
@login_required
@require_http_methods(['GET', 'POST'])
def addroom(request):
	if re.match("[bg]h[0-9]warden",str(request.user))!=None:
		h = Hostels.objects.get(username = request.user)
		a = Rooms.objects.filter(hostel=h)
		if request.method == 'POST':
			f = AddRoomForm(request.POST, request = request)
			if f.is_valid():
				room_no = f.cleaned_data.get('room_no')
				room_no = room_no.lower()
				a = Rooms(room_no=room_no,capacity_of_room=f.cleaned_data.get('capacity_of_room'),hostel=h,capacity_remaining=f.cleaned_data.get('capacity_of_room'))
				a.save()
				data['addroomform'] = f
				data['room_created'] = 'ok'
				return redirect('warden-room')
			else:
				data['addroomform'] = f
				return render(request,'warden/room.html',data)
		else:
			f = AddRoomForm()
			data['addroomform'] =  f
			return render(request,'warden/room.html',data)
	else:
		return redirect('logout')
'''@login_required
@require_http_methods(['GET', 'POST'])
def editroom(request):
	h = Hostels.objects.get(username = request.user)
	a = Rooms.objects.filter(hostel=h)
	if request.method == 'POST':
		f = AddRoomForm(request.POST, request = request)
		if f.is_valid():
			room_no = f.cleaned_data.get('room_no')
			room_no = room_no.lower()
			a = Rooms(room_no=room_no,capacity_of_room=f.cleaned_data.get('capacity_of_room'),hostel=h,capacity_remaining=f.cleaned_data.get('capacity_of_room'))
			a.save()
			#g = AddStudentForm()
			#data['addstudentform']=g
			data['addroomform'] = f
			data['room_created'] = 'ok'
			return redirect('warden-room')
		else:
			#g = AddStudentForm()
			#data['addstudentform']=g
			data['addroomform'] = f
			return render(request,'warden/room.html',data)
	else:
		f = AddRoomForm()
		#g = AddStudentForm()
		#data['addstudentform']=g
		data['addroomform'] =  f

		return render(request,'warden/room.html',data)'''

#######

'''Facilities'''

#######

def facilitybasic(user):
	basic()
	h = Hostels.objects.get(username = user)
	a = Facilities.objects.filter(hostel=h)
	facilities = []
	for i in a:
		if i.photo:
			d = {'fac':i,'photo':'yes'}
		else:
			d = {'fac':i,'photo':None}
		facilities.append(d)
	data['facilities'] = facilities
	data['editformvisible'] = None
	f = AddFacilityForm()
	data['addfacilityform'] = f

@login_required
@require_http_methods(['GET', 'POST'])
def facilities(request):
	if re.match("[bg]h[0-9]warden",str(request.user))!=None:
		facilitybasic(request.user)
		return render(request,'warden/facilities.html',data)
	else:
		return redirect('logout')

@login_required
@require_http_methods(['GET', 'POST'])
def addfacility(request):
	if re.match("[bg]h[0-9]warden",str(request.user))!=None:
		facilitybasic(request.user)
		if request.method == 'POST':
			f = AddFacilityForm(request.POST, request.FILES, user = request.user)
			if f.is_valid():
				if request.FILES.__contains__('photo'):
					fac = Facilities(title=f.cleaned_data.get('title'),description=f.cleaned_data.get('description'),hostel=Hostels.objects.get(username=request.user),photo=request.FILES.__getitem__('photo'))
				else:
					fac = Facilities(title=f.cleaned_data.get('title'),description=f.cleaned_data.get('description'),hostel=Hostels.objects.get(username=request.user))
				fac.save()
				facilitybasic(request.user)
			data['addfacilityform'] = f
			return render(request,'warden/facilities.html',data)
		else:
			return redirect('warden-facilities')
	else:
		return redirect('logout')

@login_required
@require_http_methods(['GET', 'POST'])
def editfacility(request,pk):
	if re.match("[bg]h[0-9]warden",str(request.user))!=None:
		facilitybasic(request.user)
		data['pk'] = pk
		fac = Facilities.objects.get(pk=pk)
		if request.method == 'POST':
			a = None
			a = request.FILES.__contains__('photo')
			print(request.FILES)
			print(a)
			if a:
				fac.photo.delete(True)
			f = EditFacilityForm(request.POST, request.FILES, user = request.user, pk = pk ,instance=fac)
			if f.is_valid():
				f.save()
				return redirect('warden-facilities')
			else:
				data['editfacilityform'] = f
				data['editformvisible'] = 'yes'
		else:
			g = EditFacilityForm(instance=fac)
			data['editformvisible'] = 'yes'
			data['editfacilityform'] = g
		return render(request,'warden/facilities.html',data)
	else:
		return redirect('logout')
@login_required
@require_http_methods(['GET', 'POST'])
def deletefacility(request,pk):
	if re.match("[bg]h[0-9]warden",str(request.user))!=None:
		data['pk'] = pk
		fac = Facilities.objects.get(pk=pk)
		try:
			fc=Facilities.objects.filter(pk = pk)
		except ObjectDoesNotExist:
			pass
		if fac.photo:
			fac.photo.delete(True)
		fac.delete()
		return redirect('warden-facilities')
	else:
		return redirect('logout')

#### 

'''Student'''

#######

def studentbasic(user):
	r = Rooms.objects.filter(hostel = Hostels.objects.get(username=user))
	s = Students.objects.all()
	students = []
	for i in r:
		for j in s:
			if str(i.room_no) == str(j.room_number):
				d = {'student_name':j.username, 'room_number':i.room_no, 'capacity':i.capacity_of_room}
				students.append(d)
	data['students'] = students
	return
@login_required
@require_http_methods(['GET', 'POST'])
def addstudent(request):
	if re.match("[bg]h[0-9]warden",str(request.user))!=None:
		basic()
		studentbasic(request.user)
		if request.method == 'POST':
			f = AddStudentForm(request.user,request.POST)
			if f.is_valid():
				username = f.cleaned_data.get('username')
				branch = f.cleaned_data.get('branch')
				student_email = f.cleaned_data.get('student_email')
				room_number = f.cleaned_data.get('room_number')
				user = MyUser.objects.create_user(f.cleaned_data.get('username'), '2016-02-02', f.cleaned_data.get('email'))
				user.save()
				s = Students(username = username,student_email=student_email,branch = branch, room_number = room_number)
				s.save()
				room_number.capacity_remaining-=1
				room_number.save()
				#send email to fill details
				url = "127.0.0.1:8080/student/student-details-form/" + base64.b64encode(username.encode('utf-8')).decode('utf-8')
				message = ''' Welcome To NSIT Hostel Management System. Click <a href= '%s'>here </a> to fill your details ''' % url
				email = EmailMessage('Welcome to NSIT-HMS', message, to=[student_email])
				email.send()
				data['addstudentform'] = f
				data['studentadded'] = 'ok'
				return render(request,'warden/student.html',data)
			else:
				data['addstudentform'] = f
				return render(request,'warden/student.html',data)
		else:
			f = AddStudentForm(request.user)
			data['addstudentform'] = f
			return render(request,'warden/student.html',data)
	else:
		return redirect('logout')

@login_required
@require_http_methods(['GET', 'POST'])
def student(request):
	if re.match("[bg]h[0-9]warden",str(request.user))!=None:
		basic()
		studentbasic(request.user)
		f = AddStudentForm(request.user)
		data['addstudentform'] = f
		return render(request,'warden/student.html',data)
	else:
		return redirect('logout')
