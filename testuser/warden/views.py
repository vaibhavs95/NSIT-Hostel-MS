import re
import os
import base64,random,string
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
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
from datetime import datetime,timedelta, date
from io import StringIO, BytesIO
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import letter, inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
from django_cron import CronJobBase, Schedule
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


data = {}


def basic():
	data.clear()
	a = Hostels.objects.all();
	b = []
	for i in a:
		d = {'name': i.hostel_name, 'id': i.username}
		b.append(d)
	data['all_hostels'] = b
	data['mes'] = None


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


def homebasic(request, h):
		user = Hostels.objects.get(username=h)
		data['total_rooms'] = capacity(user.username)
		data['rooms_available'] = capacityremaining(user.username)
		data['u'] = user
		g = MainDetailEditForm(instance = user)
		f = EditWardenProfileForm(request=request, instance=user)
		data['editprofileform'] = f
		data['editmaindetailform'] = g
		# return render(request,'warden/home.html',data)


@require_http_methods(['GET', 'POST'])
@login_required
def home(request):
	if re.match("[bg]h[0-9]warden", str(request.user)) != None:
		basic()
		homebasic(request, request.user)
		data['mes']=None
		try:
			a = HostelAttachDates.objects.filter(student__room_number__hostel__username = str(request.user),hostel_last_date__lte=date.today()).count()
			if a>0:
				mes = 'There are %s students who have not filled in their details yet for over 10 days.'%a
				data['mes']=mes
		except ObjectDoesNotExist:
			pass
		return render(request, 'warden/home.html', data)
	else:
		return redirect('logout')

@require_http_methods(['GET', 'POST'])
@login_required
def mainpageedit(request):
	if re.match("[bg]h[0-9]warden", str(request.user)) != None:
		basic()
		data['mes']=None
		#data['wardenphoto'] = None
		h = Hostels.objects.get(username=request.user)
		if request.method == 'POST':
			f = MainDetailEditForm(request.POST, request.FILES, instance=h)
			if f.is_valid():
				f.save()
				homebasic(request, request.user)
				return render(request, 'warden/home.html', data)
			else:
				homebasic(request, request.user)
				data['editmaindetailform'] = f
				
				#data['userid'] = h
				#if h.warden_photo:
				#	data['userid'] = h
				#	data['wardenphoto'] = 'yes'
				#else:
				#	data['userid'] = None
				return render(request, 'warden/home.html', data)
		else:
			#if h.warden_photo:
			#	data['userid'] = h
			#	data['wardenphoto'] = 'yes'
			#else:
			#	data['userid'] = None
			f = MainDetailEditForm(instance=h)
			#data['userid'] = h
			data['editmaindetailform'] = f
			return render(request, 'warden/home.html', data)
	else:
		return redirect('logout')

@require_http_methods(['GET', 'POST'])
@login_required
def profileedit(request):
	if re.match("[bg]h[0-9]warden", str(request.user)) != None:
		basic()
		data['mes']=None
		data['wardenphoto'] = None
		h = Hostels.objects.get(username=request.user)
		if request.method == 'POST':
			f = EditWardenProfileForm(request.POST, request.FILES, request=request, instance=h)
			if f.is_valid():
				f.save()
				homebasic(request, request.user)
				return render(request, 'warden/home.html', data)
			else:
				data['editprofileform'] = f
				data['userid'] = h
				if h.warden_photo:
					data['userid'] = h
					data['wardenphoto'] = 'yes'
				else:
					data['userid'] = None
				return render(request, 'warden/home.html', data)
		else:
			if h.warden_photo:
				data['userid'] = h
				data['wardenphoto'] = 'yes'
			else:
				data['userid'] = None
			f = EditWardenProfileForm(request=request, instance=h)
			data['userid'] = h
			data['editprofileform'] = f
			return render(request, 'warden/home.html', data)
	else:
		return redirect('logout')

###########

''' Rooms '''

###########


def roombasic():
	#basic()
	data['studentnotinroom'] = None
	data['studentinroom'] = None
	data['roomfulllist'] = None
	data['searchedroom'] = None
	data['searchedroomhistory'] = None
	data['searchedroomnotfound'] = None
	f = AddRoomForm()
	g = SearchRoomForm()
	data['searchroomform'] = g
	data['addroomform'] = f
	
	return


@login_required
@require_http_methods(['GET', 'POST'])
def room(request):
	if re.match("[bg]h[0-9]warden", str(request.user)) != None:
		basic()
		roombasic()
		return render(request, 'warden/room.html', data)
	else:
		return redirect('logout')


@login_required
@require_http_methods(['GET', 'POST'])
def roomall(request):
	basic()
	roombasic()
	h = Hostels.objects.get(username=request.user)
	a = (Rooms.objects.filter(hostel=h)).order_by('room_no')

	rooms = []
	for i in a:
		s = Students.objects.filter(room_number=i)
		student = []
		for j in s:
			p = {'username': j.username, 'id': base64.b64encode(
				j.username.encode('utf-8'))}
			student.append(p)
		d = {'room': i, 'students': student}
		rooms.append(d)

	paginator = Paginator(rooms, 20) # Show 1 contacts per page
	page = request.GET.get('page')
	try:
	    rooms = paginator.page(page)
	except PageNotAnInteger:
	    # If page is not an integer, deliver first page.
	    rooms = paginator.page(1)
	except EmptyPage:
	    # If page is out of range (e.g. 9999), deliver last page of results.
	    rooms = paginator.page(paginator.num_pages)

	data['rooms'] = rooms
	data['roomfulllist'] = 'yes'
	return render(request, 'warden/room.html', data)


@login_required
@require_http_methods(['GET', 'POST'])
def addroom(request):
	if re.match("[bg]h[0-9]warden", str(request.user)) != None:
		h = Hostels.objects.get(username=request.user)
		a = Rooms.objects.filter(hostel=h)
		basic()
		roombasic()
		mes = None
		if request.method == 'POST':
			f = AddRoomForm(request.POST, request=request)
			if f.is_valid():
				room_no = f.cleaned_data.get('room_no')
				room_no = room_no.upper()
				a = Rooms(room_no=room_no, capacity_of_room=f.cleaned_data.get(
					'capacity_of_room'), hostel=h, capacity_remaining=f.cleaned_data.get('capacity_of_room'))
				a.save()
				roombasic()
				mes = 'Room added successfully'
				data['addroomform'] = f
				data['mes'] = mes
				return render(request, 'warden/room.html', data)
			else:
				data['addroomform'] = f
				data['mes'] = mes
				return render(request, 'warden/room.html', data)
		else:
			f = AddRoomForm()
			data['addroomform'] = f
			data['mes'] = mes
			return render(request, 'warden/room.html', data)
	else:
		return redirect('logout')


@login_required
@require_http_methods(['GET', 'POST'])
def deleteroom(request, pk):
	if re.match("[bg]h[0-9]warden", str(request.user)) != None:
		basic()
		roombasic()
		# data['pk'] = pk
		data['mes']=None
		room = None
		try:
			room = Rooms.objects.get(pk=pk)
		except ObjectDoesNotExist:
			pass
		if room:
			hostel = room.hostel
			if str(hostel) != str(request.user):
				return redirect('logout')
		else:
			return redirect('logout')
		try:
			room = Rooms.objects.get(pk=pk)
		except ObjectDoesNotExist:
			pass
		if room.capacity_of_room == room.capacity_remaining:
			room.delete()
			data['studentnotinroom'] = 'yes'
			roombasic()
			return render(request, 'warden/room.html', data)
		else:
			data['studentinroom'] = 'yes'
			return render(request, 'warden/room.html', data)
	else:
		return redirect('logout')


@login_required
@require_http_methods(['GET', 'POST'])
def searchroom(request):
	if re.match("[bg]h[0-9]warden", str(request.user)) != None:
		h = Hostels.objects.get(username=request.user)
		basic()
		roombasic()
		if request.method == 'POST':
			f = SearchRoomForm(request.POST)
			if f.is_valid():
				room_no = f.cleaned_data.get('room_no')
				room_no = room_no.upper()
				a = None
				try:
					a = Rooms.objects.get(hostel=h, room_no=room_no)
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
				return render(request, 'warden/room.html', data)
			else:
				data['searchroomform'] = f
				return render(request, 'warden/room.html', data)
		else:
			f = SearchRoomForm()
			data['searchroomform'] = f
			return render(request, 'warden/room.html', data)
	else:
		return redirect('logout')

#######

'''Facilities'''

#######


def facilitybasic(user):
	#basic()
	h = Hostels.objects.get(username=user)
	a = Facilities.objects.filter(hostel=h)
	facilities = []
	for i in a:
		if i.photo:
			d = {'fac': i, 'photo': 'yes'}
		else:
			d = {'fac': i, 'photo': None}
		facilities.append(d)
	data['facilities'] = facilities
	data['editformvisible'] = None
	f = AddFacilityForm()
	data['addfacilityform'] = f


@login_required
@require_http_methods(['GET', 'POST'])
def facilities(request):
	if re.match("[bg]h[0-9]warden", str(request.user)) != None:
		basic()
		facilitybasic(request.user)
		return render(request, 'warden/facilities.html', data)
	else:
		return redirect('logout')


@login_required
@require_http_methods(['GET', 'POST'])
def addfacility(request):
	if re.match("[bg]h[0-9]warden", str(request.user)) != None:
		basic()
		facilitybasic(request.user)
		if request.method == 'POST':
			f = AddFacilityForm(request.POST, request.FILES, user=request.user)
			if f.is_valid():
				if request.FILES.__contains__('photo'):
					fac = Facilities(facility_name=f.cleaned_data.get('facility_name'), facility_description=f.cleaned_data.get(
						'facility_description'), hostel=Hostels.objects.get(username=request.user), photo=request.FILES.__getitem__('photo'))
				else:
					fac = Facilities(facility_name=f.cleaned_data.get('facility_name'), facility_description=f.cleaned_data.get(
						'facility_description'), hostel=Hostels.objects.get(username=request.user))
				fac.save()
				facilitybasic(request.user)
			data['addfacilityform'] = f
			return render(request, 'warden/facilities.html', data)
		else:
			return redirect('warden-facilities')
	else:
		return redirect('logout')


@login_required
@require_http_methods(['GET', 'POST'])
def editfacility(request, pk):
	if re.match("[bg]h[0-9]warden", str(request.user)) != None:
		basic()
		facilitybasic(request.user)
		data['pk'] = pk
		fac = None
		try:
			fac = Facilities.objects.get(pk=pk)
		except ObjectDoesNotExist:
			pass
		if fac:
			hostel = fac.hostel
			if str(hostel) != str(request.user):
				return redirect('logout')
		else:
			return redirect('logout')
		if request.method == 'POST':
			f = EditFacilityForm(request.POST, request.FILES,
								 request=request, user=request.user, pk=pk, instance=fac)
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
		return render(request, 'warden/facilities.html', data)
	else:
		return redirect('logout')


@login_required
@require_http_methods(['GET', 'POST'])
def deletefacility(request, pk):
	if re.match("[bg]h[0-9]warden", str(request.user)) != None:
		data['pk'] = pk
		fac = None
		try:
			fac = Facilities.objects.get(pk=pk)
		except ObjectDoesNotExist:
			pass
		if fac:
			hostel = fac.hostel
			if str(hostel) != str(request.user):
				return redirect('logout')
		else:
			return redirect('logout')
		try:
			fc = Facilities.objects.filter(pk=pk)
		except ObjectDoesNotExist:
			pass
		if fac.photo:
			fac.photo.delete(True)
		fac.delete()
		return redirect('warden-facilities')
	else:
		return redirect('logout')

#######

'''Council'''

#######


def councilbasic(user):
	#basic()
	h = Hostels.objects.get(username=user)
	a = HostelCouncil.objects.filter(hostel=h)
	council = []
	for i in a:
		if i.photo:
			d = {'coun': i, 'photo': 'yes'}
		else:
			d = {'coun': i, 'photo': None}
		council.append(d)
	data['council'] = council
	data['editformvisible'] = None
	f = AddCouncilForm()
	data['addcouncilform'] = f


@login_required
@require_http_methods(['GET', 'POST'])
def council(request):
	if re.match("[bg]h[0-9]warden", str(request.user)) != None:
		basic()
		councilbasic(request.user)
		return render(request, 'warden/council.html', data)
	else:
		return redirect('logout')


@login_required
@require_http_methods(['GET', 'POST'])
def addcouncil(request):
	if re.match("[bg]h[0-9]warden", str(request.user)) != None:
		basic()
		councilbasic(request.user)
		if request.method == 'POST':
			f = AddCouncilForm(request.POST, request.FILES, user=request.user)
			if f.is_valid():
				if request.FILES.__contains__('photo'):
					coun = HostelCouncil(name=f.cleaned_data.get('name'), email=f.cleaned_data.get('email'), phone=f.cleaned_data.get('phone'), position=f.cleaned_data.get('position'), committee=f.cleaned_data.get(
					    'committee'), hostel=Hostels.objects.get(username=request.user), photo=request.FILES.__getitem__('photo'))
				else:
					coun = HostelCouncil(name=f.cleaned_data.get('name'), email=f.cleaned_data.get('email'), phone=f.cleaned_data.get('phone'), position=f.cleaned_data.get(
					    'position'), committee=f.cleaned_data.get('committee'), hostel=Hostels.objects.get(username=request.user))
				coun.save()
				councilbasic(request.user)
			data['addcouncilform'] = f
			return render(request, 'warden/council.html', data)
		else:
			return redirect('warden-council')
	else:
		return redirect('logout')


@login_required
@require_http_methods(['GET', 'POST'])
def editcouncil(request, pk):
	if re.match("[bg]h[0-9]warden", str(request.user)) != None:
		basic()
		councilbasic(request.user)
		data['pk'] = pk
		coun = None
		try:
			coun = HostelCouncil.objects.get(pk=pk)
		except ObjectDoesNotExist:
			pass
		if coun:
			hostel = coun.hostel
			if str(hostel) != str(request.user):
				return redirect('logout')
		else:
			return redirect('logout')
		if request.method == 'POST':
			f = EditCouncilForm(request.POST, request.FILES,
								request=request, user=request.user, pk=pk, instance=coun)
			if f.is_valid():
				f.save()
				return redirect('warden-council')
			else:
				data['editcouncilform'] = f
				data['editformvisible'] = 'yes'
		else:
			g = EditCouncilForm(instance=coun)
			data['editformvisible'] = 'yes'
			data['editcouncilform'] = g
		return render(request, 'warden/council.html', data)
	else:
		return redirect('logout')


@login_required
@require_http_methods(['GET', 'POST'])
def deletecouncil(request, pk):
	if re.match("[bg]h[0-9]warden", str(request.user)) != None:
		data['pk'] = pk
		coun = None
		try:
			coun = HostelCouncil.objects.get(pk=pk)
		except ObjectDoesNotExist:
			pass
		if coun:
			hostel = coun.hostel
			if str(hostel) != str(request.user):
				return redirect('logout')
		else:
			return redirect('logout')
		try:
			co = HostelCouncil.objects.filter(pk=pk)
		except ObjectDoesNotExist:
			pass
		if coun.photo:
			coun.photo.delete(True)
		coun.delete()
		return redirect('warden-council')
	else:
		return redirect('logout')


#######

'''Forms'''

#######


def hosformbasic(user):
	#basic()
	h = Hostels.objects.get(username=user)
	a = (Form.objects.filter(hostel=h)).order_by('time')
	hosform = []
	for i in a:
		d = {'hosf': i}
		hosform.append(d)
	data['hosform'] = hosform
	data['editformvisible'] = None
	f = AddHosformForm()
	data['addhosformform'] = f


@login_required
@require_http_methods(['GET', 'POST'])
def hosform(request):
	if re.match("[bg]h[0-9]warden", str(request.user)) != None:
		basic()
		hosformbasic(request.user)
		return render(request, 'warden/hosform.html', data)
	else:
		return redirect('logout')


@login_required
@require_http_methods(['GET', 'POST'])
def addhosform(request):
	if re.match("[bg]h[0-9]warden", str(request.user)) != None:
		basic()
		hosformbasic(request.user)
		if request.method == 'POST':
			f = AddHosformForm(request.POST, request.FILES, user=request.user)
			if f.is_valid():
				# if request.FILES.__contains__('file'):
				hosf = Form(title=f.cleaned_data.get('title'), hostel=Hostels.objects.get(
					username=request.user), file=request.FILES.__getitem__('file'))
				# else:
				# hosf =
				# Form(title=f.cleaned_data.get('title'),hostel=Hostels.objects.get(username=request.user),file=request.FILES.__getitem__('file'))
				hosf.save()
				hosformbasic(request.user)
			data['addhosformform'] = f
			return render(request, 'warden/hosform.html', data)
		else:
			return redirect('warden-hosform')
	else:
		return redirect('logout')


@login_required
@require_http_methods(['GET', 'POST'])
def edithosform(request, pk):
	if re.match("[bg]h[0-9]warden", str(request.user)) != None:
		basic()
		hosformbasic(request.user)
		data['pk'] = pk
		hosf = None
		try:
			hosf = Form.objects.get(pk=pk)
		except ObjectDoesNotExist:
			pass
		if hosf:
			hostel = hosf.hostel
			if str(hostel) != str(request.user):
				return redirect('logout')
		else:
			return redirect('logout')
		if request.method == 'POST':
			a = None
			a = request.FILES.__contains__('file')
			# print(request.FILES)
			# print(a)
			if a:
				hosf.file.delete(True)
			f = EditHosformForm(
				request.POST, request.FILES, user=request.user, pk=pk, instance=hosf)
			if f.is_valid():
				f.save()
				return redirect('warden-hosform')
			else:
				data['edithosformform'] = f
				data['editformvisible'] = 'yes'
		else:
			g = EditHosformForm(instance=hosf)
			data['editformvisible'] = 'yes'
			data['edithosformform'] = g
		return render(request, 'warden/hosform.html', data)
	else:
		return redirect('logout')


@login_required
@require_http_methods(['GET', 'POST'])
def deletehosform(request, pk):
	if re.match("[bg]h[0-9]warden", str(request.user)) != None:
		data['pk'] = pk
		hosf = None
		try:
			hosf = Form.objects.get(pk=pk)
		except ObjectDoesNotExist:
			pass
		if hosf:
			hostel = hosf.hostel
			if str(hostel) != str(request.user):
				return redirect('logout')
		else:
			return redirect('logout')
		try:
			ho = Form.objects.filter(pk=pk)
		except ObjectDoesNotExist:
			pass
		if hosf.file:
			hosf.file.delete(True)
		hosf.delete()
		return redirect('warden-hosform')
	else:
		return redirect('logout')


#############

'''
Mess Details
'''

#############


def messbasic(user):
	#basic()
	h = Hostels.objects.get(username=user)
	a = MessDetail.objects.filter(hostel=h)
	if a:
		data['mess'] = a[0]
	else:
		data['mess'] = None
	data['editformvisible'] = None
	f = AddMessForm()
	data['addmessform'] = f


@login_required
@require_http_methods(['GET', 'POST'])
def mess(request):
	if re.match("[bg]h[0-9]warden", str(request.user)) != None:
		basic()
		messbasic(request.user)
		return render(request, 'warden/mess.html', data)
	else:
		return redirect('logout')


@login_required
@require_http_methods(['GET', 'POST'])
def addmess(request):
	if re.match("[bg]h[0-9]warden", str(request.user)) != None:
		basic()
		messbasic(request.user)
		if data['mess'] == None:
			if request.method == 'POST':
				f = AddMessForm(request.POST, request.FILES)
				if f.is_valid():
					a = f.save(commit=False)
					a.hostel = Hostels.objects.get(username=request.user)
					a.save()
					return mess(request)
				else:
					data['addmessform'] = f
					return render(request, 'warden/mess.html', data)
			else:
				return redirect('warden-mess')
		else:
			return redirect('warden-mess')
	else:
		return redirect('logout')


@login_required
@require_http_methods(['GET', 'POST'])
def editmess(request, pk):
	if re.match("[bg]h[0-9]warden", str(request.user)) != None:
		basic()
		messbasic(request.user)
		mess = None
		try:
			mess = MessDetail.objects.get(pk=pk)
		except ObjectDoesNotExist:
			pass
		if mess:
			hostel = mess.hostel
			if str(hostel) != str(request.user):
				return redirect('logout')
		else:
			return redirect('logout')
		if data['mess'] != None:
			data['pk'] = pk
			if request.method == 'POST':
				a = None
				a = request.FILES.__contains__('menu')
				if a:
					mess.menu.delete(True)
				f = AddMessForm(request.POST, request.FILES, instance=mess)
				if f.is_valid():
					f.save()
					return redirect('warden-mess')
				else:
					data['editmessform'] = f
					data['editformvisible'] = 'yes'
			else:
				g = AddMessForm(instance=mess)
				data['editformvisible'] = 'yes'
				data['editmessform'] = g
			return render(request, 'warden/mess.html', data)
		else:
			return redirect('warden-mess')
	else:
		return redirect('logout')


####

'''Student'''

#######


def studentbasic(user):
	#basic()
	f = AddStudentForm(user)
	data['addstudentform'] = f
	g = SearchStudentRollNoForm()
	data['searchstudentrollnoform'] = g
	h = SearchStudentOtherForm()
	data['searchstudentotherform'] = h
	data['searchedstudent'] = None
	data['searchedstudentnotfound'] = None
	data['studentfulllist'] = None
	return


@login_required
@require_http_methods(['GET', 'POST'])
def studentall(request):
	basic()
	studentbasic(request.user)
	user = request.user
	h = Hostels.objects.get(username=user)
	s = Students.objects.filter(room_number__hostel = h)
	paginator = Paginator(s, 20) # Show 1 contacts per page
	page = request.GET.get('page')
	try:
	    s = paginator.page(page)
	except PageNotAnInteger:
	    # If page is not an integer, deliver first page.
	    s = paginator.page(1)
	except EmptyPage:
	    # If page is out of range (e.g. 9999), deliver last page of results.
	    s = paginator.page(paginator.num_pages)
	data['students'] = s
	data['studentfulllist'] = 'yes'
	return render(request, 'warden/student.html', data)

@login_required
@require_http_methods(['GET', 'POST'])
def student(request):
	if re.match("[bg]h[0-9]warden", str(request.user)) != None:
		basic()
		studentbasic(request.user)
		return render(request, 'warden/student.html', data)
	else:
		return redirect('logout')


@login_required
@require_http_methods(['GET', 'POST'])
def addstudent(request):
	if re.match("[bg]h[0-9]warden", str(request.user)) != None:
		basic()
		mes = None
		if request.method == 'POST':
			print(request.user)
			f = AddStudentForm(request.user, request.POST)
			if f.is_valid():
				username = f.cleaned_data.get('username')
				branch = f.cleaned_data.get('branch')
				student_email = f.cleaned_data.get('student_email')
				room_number = f.cleaned_data.get('room_number')
				current_hostel_join_date = f.cleaned_data.get('current_hostel_join_date')				
				pas = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(10))
				s = Students(username=username, student_email=student_email, branch=branch,
							 room_number=room_number, current_hostel_join_date=current_hostel_join_date)
				user = MyUser.objects.create_user(f.cleaned_data.get(
					'username'), datetime.now(), pas)
				bank = f.cleaned_data.get('bank')
				payDate = f.cleaned_data.get('paymentDate')
				receipt = f.cleaned_data.get('receiptNumber')
				last_date = date.today()+timedelta(days=10)
				s.save()
				user.save()
				hostelAttach = HostelAttachDates(hostel_last_date = last_date,student=s)
				hostelAttach.save()
				ins = PaymentDetails(student = s,bank = bank,paymentDate = payDate,receiptNumber=receipt,paymentAmount = f.cleaned_data.get('payment_amount'))
				ins.save()
				room_number.capacity_remaining -= 1
				room_number.save()
				# send email to fill details
				url = "http://127.0.0.1:8080/student/" + \
					base64.b64encode(username.encode('utf-8')).decode('utf-8')
				message = ''' Welcome To NSIT Hostel Management System. Click <a href= '%s'>here </a> to fill your details.
				These are your login details required.
				UserId:  %s
				Password:  %s
				''' % (url,username,pas)
				email = EmailMessage('Welcome to NSIT-HMS', message, to=[student_email])
				email.send(fail_silently=True)
				mes = 'Student added successfully'
				studentbasic(request.user)
#				data['addstudentform'] = f
				data['mes'] = mes
				return render(request, 'warden/student.html', data)
			else:
				studentbasic(request.user)
				data['addstudentform'] = f
				data['mes'] = mes
				#return redirect('127.0.0.1:8000/warden/student#add')
				return render(request, 'warden/student.html', data)
		else:
			studentbasic(request.user)
			#basic()
			f = AddStudentForm(request.user)
			data['addstudentform'] = f
			data['mes'] = mes
			return render(request, 'warden/student.html', data)
	else:
		return redirect('logout')


@login_required
@require_http_methods(['GET', 'POST'])
def editstudent(request, student):
	basic()
	h = Hostels.objects.get(username=request.user)
	try:
		u = Students.objects.get(username=student)
	except:
		return redirect('warden-student')
	oldusername = u.username
	if u.room_number:
		if u.room_number.hostel == h:
			pass
		else:
			return redirect('logout')
	else:
		return redirect('logout')
	user = request.user
	if re.match("[bg]h[0-9]+warden", str(user)) != None:
		if request.method == 'POST':
			f = EditStudentForm(
				request.POST or None, request.FILES, user=request.user, username=student, instance=u)
			if f.is_valid():
				if request.FILES.__contains__('student_photo'):
					ext = request.FILES['student_photo'].name.split('.')[-1]
					filename = student
					path = settings.MEDIA_ROOT + "/student/images/" + \
						str(filename) + "." + str(ext)
					try:
						os.remove(path)
					except FileNotFoundError:
						pass
					f.student_photo = request.FILES['student_photo']
				f.save()
				newusername = f.cleaned_data.get('username')
				print(newusername)
				s = MyUser.objects.get(userid = oldusername)
				s.userid = newusername
				#a.username = newusername
				s.save()
				#a.save()
				prev = None
				crimi = None
				try:
					prev = PreviousHostelDetail.objects.filter(student=u).order_by('hostel_join_date')
				except ObjectDoesNotExist:
					pass
				try:
					i = CriminalRecord.objects.filter(student=u).order_by('date_of_action')
				except ObjectDoesNotExist:
					pass
				data['student'] = 'yes'
				data['username'] = student
				data['s'] = u
				data['prev'] = prev
				data['crim'] = crimi
				try:
					payments = PaymentDetails.objects.filter(student = u).order_by('paymentDate')
					data['paym']=payments
				except:
					pass
				return render(request, 'warden/studentProfile.html', data)
			else:
				data['form'] = f
				data['student'] = None
				data['username'] = student
				return render(request, 'warden/editstudent.html', data)
		else:
			f = EditStudentForm(user=request.user, username=student, instance=u)
			#data['student'] = 'yes'
			#data['s'] = u
			data['form'] = f
			data['username'] = student
			return render(request, 'warden/editstudent.html', data)
	else:
		return redirect('logout')


@login_required
@require_http_methods(['GET', 'POST'])
def searchstudentrollno(request):
	basic()
	studentbasic(str(request.user))
	searchedstudent = []
	h = Hostels.objects.get(username=request.user)
	if re.match("[bg]h[0-9]+warden", str(request.user)) != None:
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
						if sx.room_number.hostel == h:
							p = {'username':sx.username,'mystudent':'yes'}
						else:
							p = {'username':sx.username,}
					else:
						fine = CriminalRecord.objects.filter(student=sx,paid=False)
						if len(fine) > 0:
							p = {'username':sx}
						else:
							p = {'username':sx.username, 'freestudent':'yes'}
					searchedstudent.append(p)
				data['searchedstudent'] = searchedstudent
				data['searchstudentrollnoform'] = f
				return render(request,'warden/student.html',data)
			else:
				data['searchstudentrollnoform'] = f
				return render(request,'warden/student.html',data)
		else:

			f = SearchStudentRollNoForm()
			data['searchstudentrollnoform'] = f
			return render(request, 'warden/student.html',data)
	else:
		return redirect('logout')
@login_required
@require_http_methods(['GET', 'POST'])
def searchstudentother(request):
	basic()
	studentbasic(str(request.user))
	searchedstudent = []
	h = Hostels.objects.get(username=request.user)
	if re.match("[bg]h[0-9]+warden",str(request.user))!=None:
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
						if i.room_number:
							if i.room_number.hostel == h:
								p = {'username':i.username,'mystudent':'yes'}
							else:
								p = {'username':i.username}
						else:
							fine = CriminalRecord.objects.filter(student=i,paid=False)
							if len(fine) > 0:
								p = {'username':i.username}
							else:
								p = {'username':i.username,'freestudent':'yes'}
						searchedstudent.append(p)
				data['searchedstudent'] = searchedstudent
				data['searchstudentotherform'] = f
				return render(request,'warden/student.html',data)
			else:
				data['searchstudentotherform'] = f
				return render(request,'warden/student.html',data)
		else:
			f = SearchStudentOtherForm()
			data['searchstudentotherform'] = f
			return render(request, 'warden/student.html',data)
	else:
		return redirect('logout')
@login_required
@require_http_methods(['GET', 'POST'])
def attachstudent(request,student):
	basic()
	studentbasic(str(request.user))
	h = Hostels.objects.get(username=request.user)
	s = Students.objects.get(username=student)
	if re.match("[bg]h[0-9]+warden",str(request.user))!=None:
		if request.method == 'POST':
			f = AttachStudentForm(request.user, request.POST, instance = s)
			#searchedstudent = []
			if f.is_valid():
				bank = f.cleaned_data.get('bank')
				payDate = f.cleaned_data.get('paymentDate')
				receipt = f.cleaned_data.get('receiptNumber')
				room_number = f.cleaned_data.get('room_number')
				f.save()
				ins = PaymentDetails(student = s,bank = bank,paymentDate = payDate,receiptNumber=receipt,paymentAmount = f.cleaned_data.get('payment_amount'))
				ins.save()
				room_number.capacity_remaining -= 1
				room_number.save()
				return redirect('WardenViewStudentProfile', student=s.username)
			else:
				data['student'] = s.username
				data['attachstudentform'] = f
				return render(request,'warden/attachstudent.html',data)
		else:
			f = AttachStudentForm(request.user, instance = s)
			data['student'] = s.username
			data['attachstudentform'] = f
			return render(request, 'warden/attachstudent.html',data)
	else:
		return redirect('logout')

@login_required
@require_http_methods(['GET', 'POST'])
def printStudentList(request):
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename="studentlist.pdf"'
	buff = BytesIO()
	doc = SimpleDocTemplate(buff, pagesize=letter)
	# container for the 'Flowable' objects
	elements = []
	styles=getSampleStyleSheet()
	styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
	ptext = '<font size=20><b>STUDENT LIST</b></font>'
	elements.append(Paragraph(ptext, styles["Normal"]))
	elements.append(Spacer(1, 50))
	u = Students.objects.filter(room_number__hostel__username = request.user)
	data = []
	lst = ['Roll Number', 'Name', 'Room Number', 'Remarks']
	data.append(lst)
	for i in u:
		lst = []
		lst.append(i.username)
		if i.name != '':
			lst.append(i.name)
		else:
			lst.append('NA')
		lst.append(i.room_number)
		lst.append('')
		data.append(lst)
	t=Table(data, colWidths=[1.7*inch] * 5, hAlign='LEFT')
	t.setStyle(TableStyle([('GRID', (0,0), (-1,-1), 0.25, colors.black),]))
	elements.append(t)
	# write the document to disk
	doc.build(elements)
	response.write(buff.getvalue())
	buff.close()
	return response


@login_required
@require_http_methods(['GET', 'POST'])
def printRoomList(request):
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename="roomlist.pdf"'
	buff = BytesIO()
	doc = SimpleDocTemplate(buff, pagesize=letter)
	# container for the 'Flowable' objects
	elements = []
	styles=getSampleStyleSheet()
	styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
	ptext = '<font size=20><b>ROOM LIST</b></font>'
	elements.append(Paragraph(ptext, styles["Normal"]))
	elements.append(Spacer(1, 50))
	u = Rooms.objects.filter(hostel__username = request.user)
	data = []
	lst = ['Room Number', 'Student No. 1', 'Student No. 2', 'Student No. 3']
	data.append(lst)
	for i in u:
		b = Students.objects.filter(room_number__room_no = i.room_no, room_number__hostel__username = request.user)
		lst = []
		lst.append(i.room_no)
		for a in b:
			if a.name != '':
				s = a.name + "\n" + a.username
				lst.append(s)
			else:
				lst.append('NA' + "\n" + a.username)
		data.append(lst)
	t=Table(data, colWidths=[1.6*inch] * 4, hAlign='LEFT')
	t.setStyle(TableStyle([('GRID', (0,0), (-1,-1), 0.25, colors.black),]))
	elements.append(t)
	# write the document to disk
	doc.build(elements)
	response.write(buff.getvalue())
	buff.close()
	return response

#######
'''
Complaints
'''
#######
@login_required
@require_http_methods(['GET', 'POST'])
def forwardcomplaint(request,pk):
	if re.match("[bg]h[0-9]+warden",str(request.user))!=None:
		basic()
		data['pk'] = pk
		c = Complaints.objects.get(pk=pk)
		if request.method == 'POST':
			f = ForwardComplaintForm(request.POST)
			if f.is_valid():
				subject = f.cleaned_data.get('subject')
				body = f.cleaned_data.get('body')
				to = f.cleaned_data.get('forward_to')
				try:
					send_mail(subject, body, settings.EMAIL_HOST_USER, [to,], fail_silently=False)
					c.forwarded = True
					c.save()
				except:
					pass
				return redirect('wardenViewComplaint')
			else:
				data['forwardcomplaintform'] = f
				return render(request,'warden/forwardcomplaint.html',data)
		else:
			subject = 'Complaint in '+str(c.hostel.hostel_name)
			body = 'There is Complaint in '+str(c.hostel.hostel_name)+'\n\nPlease take a swift action to resolve it.\n\nComplaint : '+ str(c.description)+'\n Date of Complaint : '+str(c.date_of_complaint)+'\n\nWarden,'+str(c.hostel.hostel_name)
			test = {'subject' : subject, 'body': body}
			f = ForwardComplaintForm(initial = test)
			data['pk'] = pk
			data['forwardcomplaintform'] = f
			return render(request, 'warden/forwardcomplaint.html',data)
	else:
		return redirect('logout')

#############
'''
Events
'''
#############
def eventbasic(user):
	#basic()
	h = Hostels.objects.get(username=user)
	data['events'] = (Event.objects.filter(hostel=h)).order_by('time')
	f = AddEventForm()
	data['form'] = f

@login_required
@require_http_methods(['GET', 'POST'])
def event(request):
	if re.match("[bg]h[0-9]warden", str(request.user)) != None:
		basic()
		eventbasic(request.user)
		return render(request, 'warden/event.html', data)
	else:
		return redirect('logout')
@login_required
@require_http_methods(['GET', 'POST'])
def addevent(request):
	if re.match("[bg]h[0-9]warden", str(request.user)) != None:
		basic()
		eventbasic(request.user)
		print('here')
		f = AddEventForm(request.POST, request.FILES,user=request.user)
		if request.method == 'POST':
			if f.is_valid():
				f.save()
				eventbasic(request.user)
			data['form'] = f
			return render(request, 'warden/event.html', data)
		else:
			return redirect('warden-event')
	else:
		return redirect('logout')

@login_required
@require_http_methods(['GET', 'POST'])
def deleteevent(request, pk):
	if re.match("[bg]h[0-9]warden", str(request.user)) != None:
		print(pk)
		h = Hostels.objects.get(username=request.user)
		img = Images.objects.filter(event__hostel = h)
		for i in img:
			i.image.delete(True)
		e = Event.objects.get(pk=pk)
		e.delete()
		return redirect('warden-event')
	else:
		return redirect('logout')

@login_required
@require_http_methods(['GET', 'POST'])
def viewevent(request, pk):
	if re.match("[bg]h[0-9]warden", str(request.user)) != None:
		print(pk)
		basic()
		e = Event.objects.get(pk=pk)
		data['event'] = e
		data['ephotos'] = Images.objects.filter(event = e)
		return render(request,'warden/eventpage.html',data)
	else:
		return redirect('logout')

@login_required
@require_http_methods(['GET', 'POST'])
def printStuDetails(request, student_id):
	alpha = student_id
	u = Students.objects.get(username=alpha)
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename="Student Profile.pdf"'
	p = canvas.Canvas(response)


	filename = "logo.png"   # Adding LOGO
	path = settings.MEDIA_ROOT + "/" + str(filename)
	p.drawImage(path, 40, 760, 1*inch, 1 * inch)


	if u.student_photo:
	    path = settings.MEDIA_ROOT
	    path = path[:-6]
	    path = path + u.student_photo.url
	else:
	    path = settings.MEDIA_ROOT+"/"+"demo.png"
	p.drawImage(path, 400, 630, 2*inch, 2 * inch)

	p.setFont('Helvetica-Bold', 20)
	p.drawString(180, 800, "STUDENT INFO")

	p.setFont('Helvetica', 8)
	p.drawString(200, 780, "Hostel Management System")

	p.drawString(50, 750, "Roll Number:")
	p.drawString(270, 750, "%s" %u.username)

	p.drawString(50, 730, "Name:")
	p.drawString(270, 730, "%s" %u.name)

	if u.room_number:
	    p.drawString(50, 710, "Hostel:")
	    p.drawString(270, 710, "%s" %u.room_number.hostel.hostel_name)

	    p.drawString(50, 690, "Room Number:")
	    p.drawString(270, 690, "%s" %u.room_number)

	    p.drawString(50, 670, "Hostel Join Date:")
	    p.drawString(270, 670, "%s" %u.current_hostel_join_date)    
	else:
	    p.drawString(50, 710, "Hostel:")
	    p.drawString(270, 710, "None")

	    p.drawString(50, 690, "Room Number:")
	    p.drawString(270, 690, "None")

	    p.drawString(50, 670, "Hostel Join Date:")
	    p.drawString(270, 670, "None")

	p.drawString(50, 650, "Date of Birth:")
	p.drawString(270, 650, "%s" %u.date_of_birth)

	p.drawString(50, 630, "Distance from nsit:")
	p.drawString(270, 630, "%s" %u.distance_from_nsit)

	p.drawString(50, 610, "Branch:")
	p.drawString(270, 610, "%s" %u.branch)

	p.drawString(50, 590, "Gender:")
	p.drawString(270, 590, "%s" %u.gender)

	p.drawString(50, 570, "College Category:")
	p.drawString(270, 570, "%s" %u.college_category)

	p.drawString(50, 550, "Blood Group:")
	p.drawString(270, 550, "%s" %u.blood_group)

	p.drawString(50, 530, "Phone Number:")
	p.drawString(270, 530, "%s" %u.student_phone_num)

	if u.student_optional_phone_num:
	    p.drawString(50, 510, "Optional Phone Number:")
	    p.drawString(270, 510, "%s" %u.student_optional_phone_num)
	else:
	    p.drawString(50, 510, "Optional Phone Number:")
	    p.drawString(270, 510, "None")

	p.drawString(50, 490, "Students Email:")
	p.drawString(270, 490, "%s" %u.student_email)

	p.drawString(50, 470, "Father's Name:")
	p.drawString(270, 470, "%s" %u.father_name)

	p.drawString(50, 450, "Mother's Name:")
	p.drawString(270, 450, "%s" %u.mother_name)

	p.drawString(50, 430, "Parent's Email:")
	p.drawString(270, 430, "%s" %u.parent_email)

	p.drawString(50, 410, "Parent's Phone Number:")
	p.drawString(270, 410, "%s" %u.parent_phone_num)

	if u.parent_optional_phone_num:
	    p.drawString(50, 390, "Parent's Optional Phone Number:")
	    p.drawString(270, 390, "%s" %u.parent_optional_phone_num)
	else:
	    p.drawString(50, 390, "Parent's Optional Phone Number:")
	    p.drawString(270, 390, "None")


	p.drawString(50, 370, "Permanent Address:")
	p.drawString(270, 370, "%s" %u.permanent_address)

	p.drawString(50, 350, "Permanent Address Zipcode:")
	p.drawString(270, 350, "%s" %u.permanent_address_zipcode)

	p.drawString(50, 330, "Local Guardian Name:")
	p.drawString(270, 330, "%s" %u.local_guardian_name)

	p.drawString(50, 310, "Local Guardian Address:")
	p.drawString(270, 310, "%s" %u.local_guardian_address)

	p.drawString(50, 290, "Local Guardian Address Zipcode:")
	p.drawString(270, 290, "%s" %u.local_guardian_address_zipcode)

	p.drawString(50, 270, "Local Guardian Phone Number:")
	p.drawString(270, 270, "%s" %u.local_guardian_phone_num)

	if u.local_guardian_optional_phone_num:
	    p.drawString(50, 250, "Local Guardian Optional Phone Number:")
	    p.drawString(270, 250, "%s" %u.local_guardian_optional_phone_num)
	else:
	    p.drawString(50, 250, "Local Guardian Optional Phone Number:")
	    p.drawString(270, 250, "None")


	p.drawString(50, 230, "Local Guardian Email:")
	p.drawString(270, 230, "%s" %u.local_guardian_email)

	p.setFont('Helvetica-Bold', 15)
	p.drawString(50, 200, "PREVIOUS HOSTEL DETAILS")

	p.setFont('Helvetica', 8)
	cur = 160
	try:
		# print (alpha)
		prev = PreviousHostelDetail.objects.filter(student__username=alpha)
		if not prev:
			p.drawString(50, 180, "No Records Available")
		else:
			p.setFont('Helvetica-Bold', 8)
			p.drawString(50, 180, "S.No     Hostel Name          Room No.          Join Date         Leave Date")
			ctr = 1
			p.setFont('Helvetica', 8)
			for i in prev:
				p.drawString(50, cur, " %s.         %s           %s            %s        %s" %(ctr, i.hostel_name, i.room_no, i.hostel_join_date, i.hostel_leave_date))
				ctr = ctr+1
				cur = cur-20
	except ObjectDoesNotExist:
	    pass
	cur = cur-20
	p.setFont('Helvetica-Bold', 15)
	p.drawString(50, cur, "DISCIPLINARY ACTIONS")
	cur = cur-20

	p.setFont('Helvetica', 8)
	try:
	    crimi = CriminalRecord.objects.filter(student__username=alpha)
	    if not crimi:
	        p.drawString(50, cur, "No Records Available")
	    else:
	        p.setFont('Helvetica-Bold', 8)
	        p.drawString(50, cur, "S.No     Date of Action          Fine Amount          Paid or not")
	        cur = cur-20
	        ctr = 1
	        p.setFont('Helvetica', 8)
	        for i in crimi:
	            if i.paid:
	                pay = "Yes"
	            else:
	                pay = "No"
	            p.drawString(50, cur, " %s.         %s                %s                            %s" %(ctr, i.date_of_action, i.fine_amount, pay))
	            ctr = ctr+1
	            cur = cur-20
	except ObjectDoesNotExist:
	    pass

	# Close the PDF object cleanly, and we're done.
	p.showPage()
	p.save()
	return response



class MyCronJob(CronJobBase):
    RUN_EVERY_MINS=720
    # every 12 hours
    schedule = Schedule(run_every_mins =RUN_EVERY_MINS)
    code= 'student.my_cron_job'
    # a unique code
    def do(self):
    	print ("Hello from Cron")
    	h = Hostels.objects.all()
    	lst = []
    	for i in h:
    		if i.semEndDate == date.today():
    			send_mail('NSIT_HMS','Students have been detatched as Sem End Date has been reached. Check the view all students tab to find out the students who were not detatched due to some unpaid fine',settings.EMAIL_HOST_USER,[i.email,])
    			s = Students.objects.all()
    			for stu in s:
    				crimi = None
    				try:
    					crimi = CriminalRecord.objects.filter(student = stu.username)
    				except ObjectDoesNotExist:
    					pass
    				f = 0
    				for rec in crimi:
    					if rec.paid == False:
    						f = 1
    						break
    				if f == 1:
    					lst.append(stu)
    				if stu.room_number != None and stu.room_number.hostel.hostel_name == i.hostel_name and f == 0:
    					try:
    						rom = Rooms.objects.get(students__username = stu.username)
    						rom.capacity_remaining+=1
    						rom.save()
    					except ObjectDoesNotExist:
    						pass
    					stu.room_number=None
    					stu.save()
    					delta = PreviousHostelDetail(hostel_name = i.hostel_name,room_no = rom.room_no,student = stu,hostel_join_date = stu.current_hostel_join_date,
    						hostel_leave_date = date.today())
    					delta.save()