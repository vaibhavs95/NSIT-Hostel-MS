import os
from newapp.models import *
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from django.conf import settings
from django.core.mail import send_mail
h = Hostels.objects.all()
	lst = []
	x = 1
	for i in h:
		if i.semEndDate == date.today() or x == 1:
			# send_mail('NSIT_HMS','Students have been detatched as Sem End Date has been reached. Check the view all students tab to find out the students who were not detatched due to some unpaid fine',settings.EMAIL_HOST_USER,[i.email,])
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