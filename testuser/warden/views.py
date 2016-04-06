import re
import os
import base64
from django.shortcuts import render, redirect, get_object_or_404
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

from io import StringIO, BytesIO
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import letter, inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer

data = {}


def basic():
	data.clear()
	a = Hostels.objects.all();
	b = []
	for i in a:
		d = {'name': i.hostel_name, 'id': i.username}
		b.append(d)
	data['all_hostels'] = b


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
		#basic()
		user = Hostels.objects.get(username=h)
		
		data['name'] = user.name
		data['phone'] = user.phone
		data['landline'] = user.landline
		data['email'] = user.email
		data['dept'] = user.department
		data['portfolio'] = user.portfolio
		data['total_rooms'] = capacity(user.username)
		data['rooms_available'] = capacityremaining(user.username)
		if user.warden_photo:
			data['wardenphoto'] = 'yes'
			data['userid'] = user
		else:
			data['wardenphoto'] = None
			data['userid'] = None
		f = EditWardenProfileForm(request=request, instance=user)
		data['editprofileform'] = f
		# return render(request,'warden/home.html',data)


@require_http_methods(['GET', 'POST'])
@login_required
def home(request):
	if re.match("[bg]h[0-9]warden", str(request.user)) != None:
		basic()
		homebasic(request, request.user)
		data['mes']=None
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
'''@login_required
@require_http_methods(['GET', 'POST'])
def searchroomhistory(request):
	if re.match("[bg]h[0-9]warden", str(request.user)) != None:
		h = Hostels.objects.get(username=request.user)
		roombasic()
		searchedroomhistory = []
		if request.method == 'POST':
			f = SearchRoomForm(request.POST)
			if f.is_valid():
				room_no = f.cleaned_data.get('room_no')
				room_no = room_no.upper()
				his = []
				try:
					his = PreviousHostelDetail.objects.filter(hostel_name = h.hostel_name, room_no = room_no)
				except:
					pass
				if(len(his) < 1):
					data['searchedroomnotfound'] = 'yes'
				if not data['searchedstudentnotfound']:
					for k in his:
						a = Rooms.objects.get(hostel=h, room_no=k.room_no)
						s = Students.objects.filter(room_number=a)
						student = []
						for j in s:
							p = {'username': j.username, 'id': base64.b64encode(
							    j.username.encode('utf-8'))}
							student.append(p)
						d = {'room': a, 'students': student}
						searchedroomhistory.append(d)
				if len(searchedroomhistory) > 1:
					data['searchedroomhistory'] = searchedroomhistory
				else:
					data['searchedroomhistory'] = None
				data['searchroomhistoryform'] = f
				return render(request, 'warden/room.html', data)
			else:
				data['searchroomhistoryform'] = f
				return render(request, 'warden/room.html', data)
		else:
			f = SearchRoomForm()
			data['searchroomhistoryform'] = f
			return render(request, 'warden/room.html', data)
	else:
		return redirect('logout')
'''

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
			f = AddCouncilForm()
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
	r = Rooms.objects.filter(hostel=h)
	student = []
	for i in r:
		s = Students.objects.filter(room_number=i)
		for j in s:
			p = {'room': i, 'username': j.username,
				'id': base64.b64encode(j.username.encode('utf-8'))}
			student.append(p)
	data['students'] = student
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
			f = AddStudentForm(request.user, request.POST)
			if f.is_valid():
				username = f.cleaned_data.get('username')
				branch = f.cleaned_data.get('branch')
				student_email = f.cleaned_data.get('student_email')
				room_number = f.cleaned_data.get('room_number')
				current_hostel_join_date = f.cleaned_data.get('current_hostel_join_date')
				s = Students(username=username, student_email=student_email, branch=branch,
							 room_number=room_number, current_hostel_join_date=current_hostel_join_date)
				user = MyUser.objects.create_user(f.cleaned_data.get(
					'username'), '2016-02-02', f.cleaned_data.get('student_email'))
				# send email to fill details
				url = "http://127.0.0.1:8080/student/" + \
					base64.b64encode(username.encode('utf-8')).decode('utf-8')
				message = ''' Welcome To NSIT Hostel Management System. Click <a href= '%s'>here </a> to fill your details ''' % url
				email = EmailMessage('Welcome to NSIT-HMS', message, to=[student_email])
				email.send()
				s.save()
				user.save()
				room_number.capacity_remaining -= 1
				room_number.save()
				mes = 'Student added successfully'
				studentbasic(request.user)
				data['addstudentform'] = f
				data['mes'] = mes
				return render(request, 'warden/student.html', data)
			else:
				studentbasic(request.user)
				data['addstudentform'] = f
				data['mes'] = mes
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
	alpha = str(base64.b64decode(student))
	alpha = alpha[2:11]
	basic()
	#studentbasic()
	h = Hostels.objects.get(username=request.user)
	u = Students.objects.get(username=alpha)
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
				request.POST or None, request.FILES, user=request.user, username=alpha, instance=u)
			if f.is_valid():
				if request.FILES.__contains__('student_photo'):
					ext = request.FILES['student_photo'].name.split('.')[-1]
					filename = alpha
					path = settings.MEDIA_ROOT + "/student/images/" + \
						str(filename) + "." + str(ext)
					try:
						os.remove(path)
					except FileNotFoundError:
						pass
					f.student_photo = request.FILES['student_photo']
				f.save()
				prev = None
				crimi = None
				try:
					prev = PreviousHostelDetail.objects.filter(student=alpha)
				except ObjectDoesNotExist:
					pass
				try:
					i = CriminalRecord.objects.filter(student=alpha)
				except ObjectDoesNotExist:
					pass
				data['student'] = 'yes'
				data['username'] = student
				data['s'] = u
				data['prev'] = prev
				data['crim'] = crimi
				return render(request, 'student/students/studentProfile.html', data)
			else:
				data['form'] = f
				data['student'] = None
				data['username'] = student
				return render(request, 'student/students/home.html', data)
		else:
			f = EditStudentForm(user=request.user, username=alpha, instance=u)
			data['student'] = 'yes'
			data['username'] = student
			data['s'] = u
			data['form'] = f
			data['username'] = student
			return render(request, 'student/students/home.html', data)
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
							p = {'username':sx.username, 'id':base64.b64encode(sx.username.encode('utf-8')),'mystudent':'yes'}
						else:
							p = {'username':sx.username, 'id':base64.b64encode(sx.username.encode('utf-8'))}
					else:
						p = {'username':sx.username, 'id':base64.b64encode(sx.username.encode('utf-8')),'freestudent':'yes'}
					searchedstudent.append(p)
					#else:
					#    data['searchedstudentnotfound'] = 'yes'
				data['searchedstudent'] = searchedstudent
				return render(request,'warden/student.html',data)
			else:
				data['searchstudentrollnoform'] = f
				return render(request,'warden/student.html',data)
		else:

			f = SearchStudentRollNoForm()
			data['searchstudentrollnoform'] = f
			return render(request, 'student/students/home.html',data)
	else:
		return redirect('logout')
@login_required
@require_http_methods(['GET', 'POST'])
def searchstudentother(request):
	basic()
	studentbasic(str(request.user))
	h = Hostels.objects.get(username=request.user)
	if re.match("[bg]h[0-9]+warden",str(request.user))!=None:
		if request.method == 'POST':
			f = SearchStudentOtherForm(request.POST or None)
			searchedstudent = []
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
				if not data['searchedstudentnotfound'] and sx:
					for i in sx:
						if i.room_number:
							if i.room_number.hostel == h:
								p = {'username':i.username, 'id':base64.b64encode(i.username.encode('utf-8')),'mystudent':'yes'}
							else:
								p = {'username':i.username, 'id':base64.b64encode(i.username.encode('utf-8'))}
							searchedstudent.append(p)
				data['searchedstudent'] = searchedstudent
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
				room_number = f.cleaned_data.get('room_number')
				f.room_number = room_number
				f.save()
				room_number.capacity_remaining -= 1
				room_number.save()
				return redirect('warden-student')
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
	lst = ['Roll Number', 'Name', 'Room Number']
	data.append(lst)
	for i in u:
		lst = []
		lst.append(i.username)
		if i.name != '':
			lst.append(i.name)
		else:
			lst.append('NA')
		lst.append(i.room_number)
		data.append(lst)
	t=Table(data, colWidths=[1.9*inch] * 5, hAlign='LEFT')
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
		b = Students.objects.filter(room_number__room_no = i.room_no)
		lst = []
		lst.append(i.room_no)
		for a in b:
			if a.name != '':
				lst.append(a.name)
			else:
				lst.append('NA')
		data.append(lst)
	t=Table(data, colWidths=[1.6*inch] * 4, hAlign='LEFT')
	t.setStyle(TableStyle([('GRID', (0,0), (-1,-1), 0.25, colors.black),]))
	elements.append(t)
	# write the document to disk
	doc.build(elements)
	response.write(buff.getvalue())
	buff.close()
	return response
