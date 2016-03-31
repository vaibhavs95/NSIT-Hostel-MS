from django import forms
from django.forms import ModelForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate
from newapp.models import *
import re
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
        fields = ['name','phone','email','landline','department','portfolio','warden_photo']
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(EditWardenProfileForm, self).__init__(*args, **kwargs)
    def clean(self):
        name = self.cleaned_data.get('name')
        phone = self.cleaned_data.get('phone')
        landline = self.cleaned_data.get('landline')
        if name and phone and landline:
            name = name.title()
            if len(phone) == 10:
                raise forms.ValidationError('Enter Correct Phone Number without std code')
            if len(landline) == 8:
                raise forms.ValidationError('Enter Correct Landline Number without std code')
            if photocheck(self.request.FILES,'warden_photo'):
                h = Hostels.objects.get(username=self.request.user)
                h.warden_photo.delete(True)
                #pass
               # raise forms.ValidationError('Add Photo of correct format - JPG,jpeg,PNG,png,jpg,JPEG')
        return self.cleaned_data
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
            room_no = room_no.lower()
            if capacity_of_room > 3:
                raise forms.ValidationError('Capacity of Room cannot be more than three')
            h = Hostels.objects.get(username = self.request.user)
            r = Rooms.objects.filter(room_no = room_no,hostel = h)
            if(len(r) > 0):
                raise forms.ValidationError('This Room already Exists.')
        return self.cleaned_data
'''class EditRoomForm(forms.ModelForm):
    h = Hostels.objects.get(username=request.user)
    room_num = forms.ModelChoiceField(queryset = (Rooms.objects.filter(hostel = h)).order_by('room_no'),initial = 0)
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(AddRoomForm, self).__init__(*args, **kwargs)
    def clean(self):
        room_no = self.cleaned_data.get('room_no')
        capacity_of_room = self.cleaned_data.get('capacity_of_room')
        if room_no and capacity_of_room:
            room_no = room_no.lower()
            if capacity_of_room > 3:
                raise forms.ValidationError('Capacity of Room cannot be more than three')
            h = Hostels.objects.get(username = self.request.user)
            r = Rooms.objects.filter(room_no = room_no,hostel = h)
            if(len(r) > 0):
                raise forms.ValidationError('This Room already Exists.')
        return self.cleaned_data'''
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
    class Meta:
        model = Students
        fields = ['username','branch','room_number','student_email']
    def __init__(self, user, *args, **kwargs):
        super(AddStudentForm, self).__init__(*args, **kwargs)
        self.fields['room_number'].queryset = Rooms.objects.filter(capacity_remaining__gt = 0, hostel = Hostels.objects.get(username=user))
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
class AddNoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        exclude = ['creator']