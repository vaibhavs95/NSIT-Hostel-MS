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
DEPT_CHOICES = (('COE', 'Computer Science Engineering'), ('ECE', 'Electoincs Engineering'))
COLLEGE_CAT = (('DGEN','Delhi General'), ('DOBC','Delhi OBC'),('DSC','Delhi SC'),('DST','Delhi ST'))
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

class Hostels(models.Model):
	username = models.CharField(max_length = 20, primary_key = True, default='')
	name = models.CharField(max_length = 20, default='',null=True)
	hostel_name = models.CharField(max_length = 20, default='')
	room_capacity = models.IntegerField(null=True, blank=True)		# calculate from 
	room_available = models.IntegerField(null=True, blank=True)		# update with each entry
	phone = models.CharField(null = True,max_length=20, blank=True)        #Check if it has 10 digits
	email = models.EmailField(null = True, blank=True)
	landline = models.CharField(null = True, max_length = 300, blank=True)
	portfolio = models.CharField(null = True,max_length = 40, blank=True)
	department = models.CharField(null = True,max_length = 20, blank=True)
	chief_warden = models.ForeignKey(ChiefWarden)
	#warden_photo = models.nowField()	
	#admission_form = models.FileField(upload_to = get_upload_file_name)
	def __str__(self):              # __unicode__ on Python 2
		return self.username


class Branch(models.Model):
	title = models.CharField(max_length=5, null=False)
	name = models.CharField(max_length = 100, null=False)
	def __str__(self):              # __unicode__ on Python 2
		return "%s" % (self.title)

class Rooms(models.Model):
	room_no = models.CharField(null = False,max_length=10)
	capacity_of_room = models.IntegerField(null = False)
	hostel = models.ForeignKey(Hostels)
	student_no1 = models.CharField(null = True, blank = True, max_length = 300)
	student_no2 = models.CharField(null = True, blank = True, max_length = 300)
	student_no3 = models.CharField(null = True, blank = True, max_length = 300)
	capacity_remaining = models.IntegerField(null = True, blank = True)     #calculate
	def __str__(self):              # __unicode__ on Python 2
		return "%s" % (self.room_no)
class Students(models.Model):
	username = models.CharField(max_length = 20, primary_key = True , default='');
	name = models.CharField(max_length=50 , blank = True, default='');
	date_of_birth = models.DateTimeField(null=False,default = datetime.now)
	room_number = models.ForeignKey(Rooms);
	distance_from_nsit = models.IntegerField(null = False,  blank = True, default=0);
	current_sem_join_date = models.DateTimeField(default=datetime.now, blank = True,  null=True)
	current_hostel_join_date = models.DateTimeField(default=datetime.now, blank = True, null=True)
	branch = models.ForeignKey(Branch)
	gender = models.CharField(max_length = 10,  blank = True, choices = GENDER_CHOICES, default = GENDER_CHOICES[0][0])
	college_category = models.CharField(max_length=5,  blank = True, choices = COLLEGE_CAT, default = COLLEGE_CAT[0][0])
	#**hostel_category = models.CharField(null=False,max_length=20)
	blood_group = models.CharField(max_length=5,  blank = True, choices = BLOOD_GROUP, default = BLOOD_GROUP[0][0])
	fee_last_submitted = models.DateTimeField(null=True, blank = True, default = datetime.now)
	student_phone_num = models.CharField(null = False, blank = True, max_length=20)
	student_email = models.EmailField(null=False,unique=True)
	student_optional_phone_num = models.CharField(null = True, blank = True, max_length=20)
#Corpus
	corpus_calculated_uptill = models.DateTimeField(null=True, blank = True,default = datetime.now)
	corpus = models.IntegerField(null=False, blank = True, default =0)
# Family Details
	father_name = models.CharField(null=False, blank = True, max_length=100)
	mother_name = models.CharField(null=False, blank = True, max_length=100)
	parent_email = models.EmailField(null=False, blank = True)
	parent_phone_num = models.CharField(null = False, blank = True, max_length=20)
	parent_optional_phone_num = models.CharField(null = True, blank = True, max_length=20)
	permanent_address = models.CharField(null=False, blank = True, max_length=200)
	permanent_address_zipcode = models.IntegerField(null=True,  blank = True )
# Local Guradian
	local_guardian_name = models.CharField(null=True, blank = True, max_length=100)
	local_guardian_address = models.CharField(null= True, blank = True, max_length=200)
	local_guardian_address_zipcode = models.IntegerField(null=True, blank = True )
	local_guardian_phone_num = models.CharField(null = True, blank = True, max_length=20)
	local_guardian_optional_phone_num = models.CharField(null = True, blank = True, max_length=20)
	local_guardian_email = models.EmailField(null=True, blank = True )
	def __str__(self):              # __unicode__ on Python 2
		return "%s" % (self.username)
	
class MedicalHistory(models.Model):
	#code
	description = models.CharField(null=False,max_length = 250)
	student = models.ForeignKey(Students)
	def __str__(self):              # __unicode__ on Python 2
		return "%s" % (self.description)

class CriminalRecord(models.Model):
	#code
	description = models.CharField(null=False,max_length = 250)
	fine_amount = models.IntegerField(null=False)
	paid_or_not = models.BooleanField(null=False)
	date_of_action = models.DateTimeField(null=False,default = datetime.now)
	student = models.ForeignKey(Students)
	
	def __str__(self):              # __unicode__ on Python 2
		return "%s" % (self.description)
	
class PreviousHostelDetail(models.Model):
	#code
	hostel_name = models.ForeignKey(Hostels,null=False)
	room_no = models.CharField(max_length = 10, null=False)
	student = models.ForeignKey(Students,null=False)
	hostel_join_date = models.DateTimeField(null=False)
	hostel_leave_date = models.DateTimeField(null=False,default = datetime.now)
	corpus_paid = models.IntegerField(null=False)
	def __str__(self):              # __unicode__ on Python 2
		return "%s" % (self.hostel_join_date)


class Complaints(models.Model):
	lodgers_roll_no = models.CharField(null = False, max_length = 300)
	description = models.CharField(null = False, max_length = 300)
	hostel = models.ForeignKey(Hostels)
	date_of_complaint = models.DateTimeField()

	def __str__(self):              # __unicode__ on Python 2
		return "%s %s" % (self.complaint_id, self.description)

class Caretaker(models.Model):
	name_of_caretaker = models.CharField(null = False, max_length = 300)
	hostel = models.ForeignKey(Hostels)
	caretaker_phone_num = models.CharField(null = False, max_length = 300)
	#caretaker_photo = models.nowField()
	def __str__(self):              # __unicode__ on Python 2
		return "%s %s" % (self.name_of_caretaker, self.caretaker_phone_num)
		

# Create your models here.
class Facilities(models.Model):
	hostel = models.ManyToManyField(Hostels)
	title = models.CharField(null=False,max_length=100)
	description = models.TextField(null=False)
	#photo = models.nowField(upload_to="documents/%Y/%m/%d",null=False)
	def __str__(self):
		return self.title

class Closures(models.Model):
	hostel = models.ManyToManyField(Hostels)
	start_date = models.DateTimeField(null=False)
	end_date = models.DateTimeField(null=False)
	clo_or_ext = models.BooleanField(null=False)
	def __str__(self):
		closure_list = []
		closure_list.append(self.start_date)
		closure_list.append(self.end_date)
		closure_list.append(self.clo_or_ext)
		return closure_list
