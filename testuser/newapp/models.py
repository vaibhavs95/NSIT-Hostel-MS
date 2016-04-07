from django.db import models
from datetime import *
from django.utils import timezone
from django.contrib.auth.models import (
	BaseUserManager, AbstractBaseUser
)
from django.conf import settings

class MyUserManager(BaseUserManager):
	def create_user(self, userid, date_of_birth, password=None):
		"""
		Creates and saves a User with the given email, date of
		birth and password.
		"""
		if not userid:
			raise ValueError('Users must have an email address')

		user = self.model(
			userid=userid,
			date_of_birth=date_of_birth,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, userid, date_of_birth, password):
		"""
		Creates and saves a superuser with the given email, date of
		birth and password.
		"""
		user = self.create_user(userid,
			password=password,
			date_of_birth=date_of_birth
		)
		user.is_admin = True
		user.save(using=self._db)
		return user


class MyUser(AbstractBaseUser):
	userid = models.CharField(
		verbose_name='user_id',
		max_length=255,
		unique=True,
	)
	date_of_birth = models.DateField(default = timezone.now())
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)

	objects = MyUserManager()

	USERNAME_FIELD = 'userid'
	REQUIRED_FIELDS = ['date_of_birth']

	def get_full_name(self):
		# The user is identified by their email address
		return self.userid

	def get_short_name(self):
		# The user is identified by their email address
		return self.userid

	def __str__(self):              # __unicode__ on Python 2
		return self.userid

	def has_perm(self, perm, obj=None):
		"Does the user have a specific permission?"
		# Simplest possible answer: Yes, always
		return True

	def has_module_perms(self, app_label):
		"Does the user have permissions to view the app `app_label`?"
		# Simplest possible answer: Yes, always
		return True

	@property
	def is_staff(self):
		"Is the user a member of staff?"
		# Simplest possible answer: All admins are staff
		return self.is_admin
		
GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'))
MEMBER_CHOICES = (('F', 'Faculty'), ('S', 'Student'))
#DEPT_CHOICES = (('COE', 'Computer Science Engineering'), ('ECE', 'Electoincs Engineering'))
COLLEGE_CAT = (('DGEN','Delhi General'), ('DOB','Delhi OBC'),('DSC','Delhi SC'), ('DST','Delhi ST'), ('DKM','Delhi Kashmiri Migrant'), ('DDC','Delhi Defense Category'), ('DPH','Delhi Physically Handicapped'), ('DOP','Delhi OP'), 
			   ('OGEN','Outside Delhi General'), ('OOB','Outside Delhi OBC'),('OSC','Outside Delhi SC'), ('OST','Outside Delhi ST'), ('OKM','Outside Delhi Kashmiri Migrant'), ('ODC','Outside Delhi Defense Category'), ('OPH','Outside Delhi Physically Handicapped'), ('OOP','Outside Delhi OP'))
#HOSTEL_CAT = ((''))
BLOOD_GROUP = (('B+','B Positive'),('A+','A Positive'),('AB+','AB Positive'),
	('A-','A Neagtive'),('B-','B Negative'),('AB-','AB Negative'),('O+','O Positive'),('O-','O Negative'))

class ChiefWarden(models.Model):
	username = models.CharField(max_length=20, primary_key = True, default='')
	name = models.CharField(max_length=20, default='');
	email = models.EmailField(null=False)
	mobno = models.CharField(null=False, max_length = 15)
	phoneno = models.CharField(null = False,max_length=20)
	def __str__(self):
		return self.name

def warden_photo_name(instance, filename):
	ext = filename.split('.')[-1]
	return 'warden/images/hostel/'+instance.username+'.'+ext

class Hostels(models.Model):
	username = models.CharField(max_length = 20, primary_key = True, default='')
	name = models.CharField(max_length = 50, default='',null=True)
	hostel_name = models.CharField(max_length = 20, default='')
	room_capacity = models.IntegerField(null=True, blank=True)		# calculate from 
	room_available = models.IntegerField(null=True, blank=True)		# update with each entry
	phone = models.CharField(null = True,max_length=20, blank=True)        #Check if it has 10 digits
	email = models.EmailField(null = True, blank=True)
	landline = models.CharField(null = True, max_length = 300, blank=True)
	portfolio = models.CharField(null = True,max_length = 40, blank=True)
	department = models.CharField(null = True,max_length = 20, blank=True)
	chief_warden = models.ForeignKey(ChiefWarden)
	warden_photo = models.ImageField(upload_to = warden_photo_name, null = True, blank = True)	
	#admission_form = models.FileField(upload_to = get_upload_file_name)
	def __str__(self):              # __unicode__ on Python 2
		return self.username

class Branch(models.Model):
	title = models.CharField(max_length = 20, primary_key = True, null=False, default='')
	name = models.CharField(max_length = 100, null=False,default = 'COMPUTER SCIENCE AND ENGINEERING')
	roll_code = models.CharField(max_length = 5,null = False, default='')
	def __str__(self):
		return "%s" % (self.title)

class Rooms(models.Model):
	room_no = models.CharField(null = False,max_length=10)
	capacity_of_room = models.IntegerField(null = False)
	hostel = models.ForeignKey(Hostels)
	capacity_remaining = models.IntegerField(null = True, blank = True)
	def __str__(self):              # __unicode__ on Python 2
		return "%s" % (self.room_no)

def student_photo_name(instance, filename):
	ext = filename.split('.')[-1]
	return 'student/images/'+instance.username+'.'+ext
class Students(models.Model):
	username = models.CharField(max_length = 20, primary_key = True , default='');
	name = models.CharField(max_length=50 , null = False, default='');
	date_of_birth = models.DateField(null=False,default=timezone.now())
	room_number = models.ForeignKey(Rooms,null = True);
	distance_from_nsit = models.IntegerField(null = False, default=0);
	# current_sem_join_date = models.DateField(default=datetime.now, blank = True,  null=True)
	current_hostel_join_date = models.DateField(default=datetime.now, blank = True)
	valid_upto = models.DateField(blank = True,default=datetime.now)
	branch = models.ForeignKey(Branch)
	gender = models.CharField(max_length = 10, choices = GENDER_CHOICES, default = GENDER_CHOICES[0][0])
	college_category = models.CharField(max_length=5, choices = COLLEGE_CAT, default = COLLEGE_CAT[0][0])
	#**hostel_category = models.CharField(null=False,max_length=20)
	blood_group = models.CharField(max_length=5, choices = BLOOD_GROUP, default = BLOOD_GROUP[0][0])
	# fee_last_submitted = models.DateField(null=True, blank = True, default = datetime.now)
	student_phone_num = models.CharField(null = False, max_length=20)
	student_email = models.EmailField(null=False,unique=True)
	student_optional_phone_num = models.CharField(null = True, blank = True, max_length=20)
#Corpus
	# corpus_calculated_uptill = models.DateField(null=True, blank = True,default = datetime.now)
	# corpus = models.IntegerField(null=False, blank = True, default =0)
# Family Details
	father_name = models.CharField(null=False, max_length=100)
	mother_name = models.CharField(null=False, max_length=100)
	parent_email = models.EmailField(null=False)
	parent_phone_num = models.CharField(null = False, max_length=20)
	parent_optional_phone_num = models.CharField(null = True, blank = True, max_length=20)
	permanent_address = models.CharField(null=False, max_length=200)
	permanent_address_zipcode = models.IntegerField(null=True,  blank = True )
# Local Guradian
	local_guardian_name = models.CharField(null=False, max_length=100)
	local_guardian_address = models.CharField(null= False, max_length=200)
	local_guardian_address_zipcode = models.IntegerField(null=False)
	local_guardian_phone_num = models.CharField(null = False, max_length=20)
	local_guardian_optional_phone_num = models.CharField(null = False, blank = True, max_length=20)
	local_guardian_email = models.EmailField(null=False)
	student_photo = models.ImageField(upload_to=student_photo_name, null = True, blank = True)
	def __str__(self):              # __unicode__ on Python 2
		return "%s" % (self.username)

	
class HostelAttachDates(models.Model):
	hostel_join_date = models.DateField(blank=False,default=datetime.now)
	student = models.ForeignKey(Students,null=False)
	def __str__(self):
		return '%s, %s'%(self.hostel_join_date,self.student)

class Banks(models.Model):
	"""docstring for Banks"models.Model
	def __init__(self, arg):
		super(Banks,models.Model).__init__()
		self.arg = arg"""
	name = models.CharField(null=False,max_length = 100,default = '',unique = True)
	def __str__(self):
		return '%s'%(self.name)
		
class MedicalHistory(models.Model):
	#code
	description = models.CharField(null=False,max_length = 250)
	student = models.ForeignKey(Students)
	def __str__(self):              # __unicode__ on Python 2
		return "%s" % (self.description)

def CriminalRecordFile(instance, filename):
	ext = filename.split('.')[-1]
	desc = instance.description.replace(' ','')
	da = str(instance.date_of_action).replace(' ','')
	return 'newapp/files/notices/'+str(instance.student)+'/'+desc+da+'.'+ext

class CriminalRecord(models.Model):
	#code
	student = models.ForeignKey(Students)
	description = models.CharField(null=False,max_length = 400)
	fine_amount = models.IntegerField(null=False)
	paid = models.BooleanField(null=False,default = False)
	date_of_action = models.DateField(null=False)
	file = models.FileField(upload_to = CriminalRecordFile,blank = False)
	
	def __str__(self):              # __unicode__ on Python 2
		return "%s" % (self.description)
	
class PaymentDetails(models.Model):
	student = models.ForeignKey(Students,null = False)
	bank = models.ForeignKey(Banks,null = False)
	paymentDate = models.DateField(null=False)
	receiptNumber = models.IntegerField(null=False)

	def __str__(self):
		return "%s, %s"%(self.student,self.paymentDate)

class PreviousHostelDetail(models.Model):
	#code
	hostel_name = models.CharField(null=False,max_length = 40)
	room_no = models.CharField(max_length = 10, null=False)
	student = models.ForeignKey(Students,null=False)
	hostel_join_date = models.DateField(null=False)
	hostel_leave_date = models.DateField(null=False,default = datetime.now)
	# corpus_paid = models.IntegerField(null=False)
	def __str__(self):              # __unicode__ on Python 2
		return "%s" % (self.hostel_join_date)


class Complaints(models.Model):
	lodgers_roll_no = models.CharField(null = False, max_length = 300)
	description = models.CharField(null = False, max_length = 300,default = '')
	hostel = models.ForeignKey(Hostels)
	date_of_complaint = models.DateField(auto_now=True)
	closed = models.BooleanField(default = False)

	def __str__(self):              # __unicode__ on Python 2
		return "%s" % (self.description)
		
#this table holds details of caretakers, mess/hostel secretary, sports/mess/library/cultural/etc. committee and its members
def council_photo_name(instance, filename):
	ext = filename.split('.')[-1]
	return 'warden/images/council/'+instance.hostel.username+'/'+instance.position+'.'+ext
class HostelCouncil(models.Model):
	hostel = models.ForeignKey(Hostels)
	name = models.CharField(null=True,blank=True,max_length=100,default='')
	email = models.EmailField(null=False)
	phone = models.CharField(max_length=15,default='',null=False,blank=False)
	position = models.CharField(max_length=100, default='')
	committee = models.CharField(max_length=100, default='', null=True,blank=True)
	photo = models.ImageField(upload_to = council_photo_name, null = True, blank = True)
	def __str__(self):
		return self.name
def messmenu_file_name(instance, filename):
	ext = filename.split('.')[-1]
	return 'warden/files/messmenu/'+instance.hostel.username+'.'+ext
class MessDetail(models.Model):
	hostel = models.ForeignKey(Hostels)
	weekday_breakfast_from = models.TimeField(null=False)
	weekday_breakfast_to = models.TimeField(null=False)
	weekday_lunch_from = models.TimeField(null=False)
	weekday_lunch_to = models.TimeField(null=False)
	weekday_snack_from = models.TimeField(null=False)
	weekday_snack_to = models.TimeField(null=False)
	weekday_dinner_from = models.TimeField(null=False)
	weekday_dinner_to = models.TimeField(null=False)
	weekend_breakfast_from = models.TimeField(null=False)
	weekend_breakfast_to = models.TimeField(null=False)
	weekend_lunch_from = models.TimeField(null=False)
	weekend_lunch_to = models.TimeField(null=False)
	weekend_snack_from = models.TimeField(null=False)
	weekend_snack_to = models.TimeField(null=False)
	weekend_dinner_from = models.TimeField(null=False)
	weekend_dinner_to = models.TimeField(null=False)
	weekday_breakfast_charge = models.IntegerField(null=False)
	weekday_lunch_charge = models.IntegerField(null=False)
	weekday_snack_charge = models.IntegerField(null=False)
	weekday_dinner_charge = models.IntegerField(null=False)
	weekend_breakfast_charge = models.IntegerField(null=False)
	weekend_lunch_charge = models.IntegerField(null=False)
	weekend_snack_charge = models.IntegerField(null=False)
	weekend_dinner_charge = models.IntegerField(null=False)
	menu = models.FileField(upload_to=messmenu_file_name,null=False)
def form_file_name(instance, filename):
	ext = filename.split('.')[-1]
	return 'warden/files/forms/'+instance.hostel.username+'/'+instance.title+'.'+ext
class Form(models.Model):
	hostel = models.ForeignKey(Hostels)
	title = models.CharField(max_length=200,default='')
	time = models.DateTimeField(auto_now_add=True)
	file = models.FileField(upload_to = form_file_name)
# Create your models here.
def facility_photo_name(instance, filename):
	ext = filename.split('.')[-1]
	return 'warden/images/facilities/'+instance.hostel.username+'/'+instance.facility_name+'.'+ext
class Facilities(models.Model):
	hostel = models.ForeignKey(Hostels)
	facility_name = models.CharField(null=False, unique=True, max_length=100,default='')
	facility_description = models.TextField(null=False, default='')
	photo = models.ImageField(upload_to=facility_photo_name,null=True, blank=True)
	def __str__(self):
		return self.facility_name

class Closures(models.Model):
	hostel = models.ManyToManyField(Hostels)
	start_date = models.DateField(null=False)
	end_date = models.DateField(null=False)
	clo_or_ext = models.BooleanField(null=False)
	def __str__(self):
		closure_list = []
		closure_list.append(self.start_date)
		closure_list.append(self.end_date)
		closure_list.append(self.clo_or_ext)
		return closure_list

def noticePhotoForm(instance, filename):
	ext = filename.split('.')[-1]
	title = instance.title.replace(" ",'')
	return 'newapp/files/notices/'+instance.creator+'/'+title+'.'+ext

class Notice(models.Model):
    #code
	title = models.CharField(null=False, max_length = 200,default = None,unique = True)
	file = models.FileField(upload_to = noticePhotoForm,null = True)
	creator = models.CharField(max_length = 30,null = False)
