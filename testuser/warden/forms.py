from django import forms
from django.forms import ModelForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate
from newapp.models import *
import re
from django.contrib.admin.widgets import AdminDateWidget
from datetime import date,datetime
from multiupload.fields import MultiFileField

def photocheck(requestfiles,field):
    a = None
    a = requestfiles.__contains__(field)
    if a:
        name = requestfiles[field].name
        name = name.split('.')[-1]
        name = name.lower()
        print(name)
        if name == 'jpeg' or name == 'png' or name == 'jpg':
            return True
        else:
            return False
class EditWardenProfileForm(forms.ModelForm):
    class Meta:
        model = Hostels
        fields = ['name','phone','email','landline','department','portfolio','semEndDate','warden_photo']
        widgets = {
        'semEndDate':AdminDateWidget,
        }
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(EditWardenProfileForm, self).__init__(*args, **kwargs)
        self.fields['semEndDate'].required = True
    def clean(self):
        name = self.cleaned_data.get('name')
        phone = self.cleaned_data.get('phone')
        landline = self.cleaned_data.get('landline')
        if name and phone and landline:
            name = name.title()
            if len(phone) != 10:
                raise forms.ValidationError('Enter Correct Phone Number without std code')
            if len(landline) != 8:
                raise forms.ValidationError('Enter Correct Landline Number without std code')
            if photocheck(self.request.FILES,'warden_photo'):
                h = Hostels.objects.get(username=self.request.user)
                h.warden_photo.delete(True)
                #pass
               # raise forms.ValidationError('Add Photo of correct format - JPG,jpeg,PNG,png,jpg,JPEG')
        return self.cleaned_data

    def clean_semEndDate(self):
        semEndDate = self.cleaned_data.get('semEndDate')
        if semEndDate<=date.today():
            raise forms.ValidationError('This date has to be in future')
        else:
            return semEndDate

class AddRoomForm(forms.Form):
    room_no = forms.CharField(max_length=10)
    capacity_of_room = forms.IntegerField()
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(AddRoomForm, self).__init__(*args, **kwargs)
    def clean(self):
        room_no = self.cleaned_data.get('room_no')
        capacity_of_room = self.cleaned_data.get('capacity_of_room')
        if room_no and capacity_of_room:
            room_no = room_no.upper()
            if re.match("[A-Z]+-[0-9]+",str(room_no))==None:
                raise forms.ValidationError('Enter Room Number in correct format: AA-111')
            if capacity_of_room > 3:
                raise forms.ValidationError('Capacity of Room cannot be more than three')
            h = Hostels.objects.get(username = self.request.user)
            r = Rooms.objects.filter(room_no = room_no,hostel = h)
            if(len(r) > 0):
                raise forms.ValidationError('This Room already Exists.')
        return self.cleaned_data


class SearchRoomForm(forms.Form):
    room_no = forms.CharField(max_length=10,help_text='Search Room by Room Number, format : AA-111')
    def __init__(self, *args, **kwargs):
        super(SearchRoomForm, self).__init__(*args, **kwargs)
    def clean(self):
        room_no = self.cleaned_data.get('room_no')
        if room_no:
            room_no = room_no.upper()
            if re.match("[A-Z]+-[0-9]+",str(room_no))==None:
                raise forms.ValidationError('Enter Room Number in correct format: AA-111')
        else:
            raise forms.ValidationError('Room Number cannot be empty.')
        return self.cleaned_data



class AddFacilityForm(forms.ModelForm):
    class Meta:
        model = Facilities
        fields = ['facility_name','facility_description','photo']
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user',None)
        super(AddFacilityForm, self).__init__(*args, **kwargs)
    def clean(self):
        facility_name = self.cleaned_data.get('facility_name')
        userid = Hostels.objects.get(username=self.user)
        e = Facilities.objects.filter(hostel=userid)
        for i in e:
            if i.facility_name.lower() == facility_name.lower():
                raise forms.ValidationError('Facility with same title is already there')
        return self.cleaned_data

class EditFacilityForm(forms.ModelForm):
    class Meta:
        model = Facilities
        fields = ['facility_name','facility_description','photo']
    def __init__(self, *args, **kwargs):
        self.pk = kwargs.pop('pk', None)
        self.user = kwargs.pop('user',None)
        self.request = kwargs.pop('request',None)
        super(EditFacilityForm, self).__init__(*args, **kwargs)
    def clean(self):
        hostel = Facilities.objects.get(pk=self.pk).hostel
        facility_name = self.cleaned_data.get('facility_name')
        userid = Hostels.objects.get(username=self.user)
        e = Facilities.objects.filter(hostel=userid)
        for i in e:
            if int(i.pk) != int(self.pk):
                if i.facility_name.lower() == facility_name.lower():
                    raise forms.ValidationError('Facility with same facility_name is already there')
        if photocheck(self.request.FILES,'photo'):
            fac = Facilities.objects.get(pk=self.pk)
            fac.photo.delete(True)
        return self.cleaned_data

class AddCouncilForm(forms.ModelForm):
    class Meta:
        model = HostelCouncil
        fields = ['committee','position','name','phone','email','photo']
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user',None)
        super(AddCouncilForm, self).__init__(*args, **kwargs)
    def clean(self):
        committee = self.cleaned_data.get('committee')
        position = self.cleaned_data.get('position')
        phone = self.cleaned_data.get('phone')
        name = self.cleaned_data.get('name')
        userid = Hostels.objects.get(username=self.user)
        e = HostelCouncil.objects.filter(hostel=userid)
        for i in e:
            if i.position.lower() == position.lower() and i.name.lower() == name.lower():
                raise forms.ValidationError('Council Member with same name and position is already there')
            if committee == '' or committee == None:
                self.cleaned_data['committee'] = position
            if len(phone) > 10:
                raise forms.ValidationError('Enter Correct Phone Number without std code')
        return self.cleaned_data

class EditCouncilForm(forms.ModelForm):
    class Meta:
        model = HostelCouncil
        fields = ['committee','position','name','phone','email','photo']
    def __init__(self, *args, **kwargs):
        self.pk = kwargs.pop('pk', None)
        self.user = kwargs.pop('user',None)
        self.request = kwargs.pop('request',None)
        super(EditCouncilForm, self).__init__(*args, **kwargs)
    def clean(self):
        hostel = HostelCouncil.objects.get(pk=self.pk).hostel
        if str(hostel) != str(self.user):
            raise forms.ValidationError('Invalid Request')
        else:
            committee = self.cleaned_data.get('committee')
            position = self.cleaned_data.get('position')
            phone = self.cleaned_data.get('phone')
            name = self.cleaned_data.get('name')
            userid = Hostels.objects.get(username=self.user)
            e = HostelCouncil.objects.filter(hostel=userid)
            for i in e:
                if i.position.lower() == position.lower() and i.name.lower() == name.lower() and int(i.pk) != int(self.pk):
                    raise forms.ValidationError('Council Member with same name and position is already there')
                if len(phone) > 10:
                    raise forms.ValidationError('Enter Correct Phone Number without std code')
            if photocheck(self.request.FILES,'photo'):
                coun = HostelCouncil.objects.get(pk=self.pk)
                coun.photo.delete(True)
            return self.cleaned_data

class AddHosformForm(forms.ModelForm):
    class Meta:
        model = Form
        fields = ['title','file']
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user',None)
        super(AddHosformForm, self).__init__(*args, **kwargs)
    def clean(self):
        title = self.cleaned_data.get('title')
        userid = Hostels.objects.get(username=self.user)
        e = Form.objects.filter(hostel=userid)
        for i in e:
            if i.title.lower() == title.lower():
                raise forms.ValidationError('Form with same title is already there')
        return self.cleaned_data

class EditHosformForm(forms.ModelForm):
    class Meta:
        model = Form
        fields = ['title','file']
    def __init__(self, *args, **kwargs):
        self.pk = kwargs.pop('pk', None)
        self.user = kwargs.pop('user',None)
        super(EditHosformForm, self).__init__(*args, **kwargs)
    def clean(self):
        #hostel = Form.objects.get(pk=self.pk).hostel
        title = self.cleaned_data.get('title')
        userid = Hostels.objects.get(username=self.user)
        e = Form.objects.filter(hostel=userid)
        for i in e:
            if int(i.pk) != int(self.pk):
                if i.title.lower() == title.lower():
                    raise forms.ValidationError('Form with same title is already there')
        return self.cleaned_data

class AddMessForm(forms.ModelForm):
    class Meta:
        model = MessDetail
        exclude = ['hostel']
    def __init__(self,*args, **kwargs):
        super(AddMessForm, self).__init__(*args, **kwargs)
    def clean(self):
        return self.cleaned_data


class AddStudentForm(forms.ModelForm):
    paymentDate = forms.DateField(required=True)
    receiptNumber = forms.IntegerField(required = True)
    bank = forms.ModelChoiceField(required = True,queryset = Banks.objects.all())
    payment_amount = forms.IntegerField(required = True)
    class Meta:
        model = Students
        fields = ['username','branch','room_number','student_email','current_hostel_join_date']+['bank','receiptNumber','payment_amount','paymentDate']
        widgets = {
            'current_hostel_join_date': AdminDateWidget(),
            'paymentDate':AdminDateWidget(),
        }
    def __init__(self, user, *args, **kwargs):
        super(AddStudentForm, self).__init__(*args, **kwargs)
        self.fields['room_number'].queryset = Rooms.objects.filter(capacity_remaining__gt = 0, hostel = Hostels.objects.get(username=user))
        self.fields['username'].help_text='Roll No: 111-CO-16'
        self.fields['branch'].help_text='Select one from dropdown'
        self.fields['room_number'].help_text='Select one from dropdown'
        self.fields['current_hostel_join_date'].help_text='Format: yyyy-mm-dd hh:mm:ss'
        self.user = user
    def clean(self):
        username = self.cleaned_data.get('username')
        branch = self.cleaned_data.get('branch')
        student_email = self.cleaned_data.get('student_email')
        room_number = self.cleaned_data.get('room_number')
        if username and branch and student_email and room_number:
            if re.match("[0-9]*-[A-Z]*-[0-9]*",str(username)) != None:
                s = None
                u = None
                try:
                    s = Students.objects.get(username=username)
                except ObjectDoesNotExist:
                    pass
                try:
                    u = MyUser.objects.get(userid=username)
                except ObjectDoesNotExist:
                    pass
                if s is not None or u is not None:
                    raise forms.ValidationError('Student Alredy Exists')
                e = Students.objects.all()
                for i in e:
                    if i.student_email == student_email:
                        raise forms.ValidationError('Email is already registered')
            else:
                raise forms.ValidationError('Incorrect format of username.(Correct format: 111-CO-15)')
        return self.cleaned_data

    def clean_current_hostel_join_date(self):
        date = self.cleaned_data.get('current_hostel_join_date')
        try:
            a = Hostels.objects.get(username = self.user)
            a = a.semEndDate
        except ObjectDoesNotExist:
            pass
        if date>date.today():
            raise forms.ValidationError('Join date can\'t be in future')
        elif date>a:
            raise forms.ValidationError('You might want to change sem end date, join date can\'t be greater than sem end date')
        else:
            return date

    def clean_paymentDate(self):
        date = self.cleaned_data.get('paymentDate')
        try:
            a = Hostels.objects.get(username = self.user)
            a=a.semEndDate
        except ObjectDoesNotExist:
            pass
        if date>date.today():
            raise forms.ValidationError('Payment date can\'t be in future')
        elif date>a:
            raise forms.ValidationError('You might want to change sem end date, payment date can\'t be greater than sem end date')
        else:
            return date

    def clean_payment_amount(self):
        pay = self.cleaned_data.get('payment_amount')
        if pay < 0:
            raise forms.ValidationError('This field has to be non-negative value')
        else:
            return pay

class EditStudentForm(forms.ModelForm):
    class Meta:
        model = Students
        exclude = ['room_number']
#        fields = '__all__'
        widgets = {
            'current_hostel_join_date': AdminDateWidget(),
            'date_of_birth' : AdminDateWidget(),
        }
    def __init__(self, *args, **kwargs):
        self.username = kwargs.pop('username', None)
        self.user = kwargs.pop('user',None)
        super(EditStudentForm, self).__init__(*args, **kwargs)
        self.fields['branch'].help_text='Select one from dropdown'
        self.fields['current_hostel_join_date'].help_text='Format: yyyy-mm-dd hh:mm:ss'
    def clean(self):
        student_phone_num = self.cleaned_data.get('student_phone_num')
        parent_phone_num = self.cleaned_data.get('parent_phone_num')
        local_guardian_phone_num = self.cleaned_data.get('local_guardian_phone_num')
        student_email = self.cleaned_data.get('student_email')
        if len(str(student_phone_num)) == 10 and len(str(parent_phone_num)) == 10 and len(str(local_guardian_phone_num)) == 10:
            pass
        else:
            raise forms.ValidationError('Enter a valid 10 digit phone number')
        e = Students.objects.all()
        for i in e:
            if i.student_email == student_email and i.username != self.username:
                raise forms.ValidationError('Email is already registered')
        return self.cleaned_data
class SearchStudentRollNoForm(forms.Form):
    roll_no = forms.CharField(max_length=10,help_text='Search Student by Roll Number, format : 111-AA-11')
    def __init__(self, *args, **kwargs):
        super(SearchStudentRollNoForm, self).__init__(*args, **kwargs)
    def clean(self):
        roll_no = self.cleaned_data.get('roll_no')
        if re.match("[0-9]+-[A-Z]+-[0-9]",str(roll_no)) == None:
            raise forms.ValidationError('Enter Roll Number in correct format: 111-AA-11')
        return self.cleaned_data
class SearchStudentOtherForm(forms.Form):
    name = forms.CharField(max_length=100, required = False)
    date_of_birth = forms.DateField(widget = AdminDateWidget(), required = False)
    def __init__(self, *args, **kwargs):
        super(SearchStudentOtherForm, self).__init__(*args, **kwargs)
    def clean(self):
        name = self.cleaned_data.get('name')
        date_of_birth = self.cleaned_data.get('date_of_birth')
        if name or date_of_birth:
            pass
        else:
            raise forms.ValidationError('Search Fields Cannot be empty')
        #if re.match("[0-9]+-[A-Z]+-[0-9]",str(roll_no)) == None:
        #    raise forms.ValidationError('Enter Roll Number in correct format: 111-AA-11')
        return self.cleaned_data
class AttachStudentForm(forms.ModelForm):
    paymentDate = forms.DateField(required=True)
    receiptNumber = forms.IntegerField(required = True)
    bank = forms.ModelChoiceField(required = True,queryset = Banks.objects.all())
    payment_amount = forms.IntegerField(required=True)
    class Meta:
        model = Students
        fields = ['username', 'room_number','current_hostel_join_date']+['bank','receiptNumber','payment_amount','paymentDate']
        widgets = {
            'current_hostel_join_date': AdminDateWidget(),
            'paymentDate':AdminDateWidget(),
        }
    def __init__(self, user, *args, **kwargs):
        #self.user = kwargs.pop('user')
        super(AttachStudentForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['readonly'] = True
        self.fields['room_number'].queryset = Rooms.objects.filter(capacity_remaining__gt = 0, hostel = Hostels.objects.get(username=user))
        self.user = user
    def clean(self):
        pay=self.cleaned_data.get('payment_amount')
        if pay <0:
            raise forms.ValidationError('This field has to be non-negative value')
        return self.cleaned_data

    def clean_paymentDate(self):
        date = self.cleaned_data.get('paymentDate')
        try:
            a = Hostels.objects.get(username = self.user)
            a=a.semEndDate
        except ObjectDoesNotExist:
            pass
        if date>date.today():
            raise forms.ValidationError('Payment date can\'t be in future')
        elif date>a:
            raise forms.ValidationError('You might want to change sem end date, payment date can\'t be greater than sem end date')
        else:
            return date

class AddNoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        exclude = ['creator','date']

class DetachStudentForm(forms.ModelForm):
    hostel_leave_date = forms.DateField(required = True)
    class Meta:
        model = Students
        fields = ['username']+['hostel_leave_date']
        widgets = {
            'hostel_leave_date':AdminDateWidget(),
        }
    def __init__(self, user, *args, **kwargs):
        #self.user = kwargs.pop('user')
        super(DetachStudentForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['readonly'] = True
        # self.fields['room_number'].widget.attrs['disabled'] = 'disabled'

    def clean_hostel_leave_date(self):
        date = self.cleaned_data.get('hostel_leave_date')
        if date>date.today():
            raise forms.ValidationError('This field can\'t be in future')
        return date

class AddCriminalForm(forms.ModelForm):
    class Meta:
        model = CriminalRecord
        exclude = ['student']
        widgets = {
            'date_of_action':AdminDateWidget(),
        }

class ForwardComplaintForm(forms.Form):
    forward_to = forms.EmailField()
    subject = forms.CharField(max_length = 100)
    body = forms.CharField(max_length = 500,widget=forms.Textarea)
    def __init__(self, *args, **kwargs):
        super(ForwardComplaintForm, self).__init__(*args, **kwargs)
    def clean(self):
        return self.cleaned_data


class AddEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description','time']  # not attachments!
        widgets = {
            'description': forms.Textarea(attrs={'class': 'input-field'})
        }
    images = MultiFileField(min_num=0, max_num=150, max_file_size=1024*1024*5)
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user',None)
        super(AddEventForm, self).__init__(*args, **kwargs)
        self.fields['description'].required=True
        self.fields['title'].required=True
        self.fields['images'].required=False
    def save(self, commit=True):
        instance = super(AddEventForm, self).save(commit=False)
        print(instance)
        print(instance.title)
        instance.hostel = Hostels.objects.get(username=self.user)
        instance.save(commit)
        for each in self.cleaned_data['images']:
            Images.objects.create(image=each, event=instance)
        return instance
class MainDetailEditForm(forms.ModelForm):
    class Meta:
        model = Hostels
        fields = ['hostel_text','hostel_photo']
    def __init__(self, *args, **kwargs):
        super(MainDetailEditForm, self).__init__(*args, **kwargs)
    def clean(self):
        return self.cleaned_data
class EditWardenProfileForm(forms.ModelForm):
    class Meta:
        model = Hostels
        fields = ['name','phone','email','landline','department','portfolio','semEndDate','warden_photo']
        widgets = {
        'semEndDate':AdminDateWidget,
        }
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(EditWardenProfileForm, self).__init__(*args, **kwargs)
        self.fields['semEndDate'].required = True
    def clean(self):
        name = self.cleaned_data.get('name')
        phone = self.cleaned_data.get('phone')
        landline = self.cleaned_data.get('landline')
        if name and phone and landline:
            name = name.title()
            if len(phone) != 10:
                raise forms.ValidationError('Enter Correct Phone Number without std code')
            if len(landline) != 8:
                raise forms.ValidationError('Enter Correct Landline Number without std code')
            if photocheck(self.request.FILES,'warden_photo'):
                h = Hostels.objects.get(username=self.request.user)
                h.warden_photo.delete(True)
                #pass
               # raise forms.ValidationError('Add Photo of correct format - JPG,jpeg,PNG,png,jpg,JPEG')
        return self.cleaned_data
