from django import forms
from django.forms import ModelForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate
from newapp.models import *
import re

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
            if len(phone) > 10:
                raise forms.ValidationError('Enter Correct Phone Number without std code')
            if len(landline) > 8:
                raise forms.ValidationError('Enter Correct Landline Number without std code')
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
        fields = ['title','description','photo']
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user',None)
        super(AddFacilityForm, self).__init__(*args, **kwargs)
    def clean(self):
        title = self.cleaned_data.get('title')
        userid = Hostels.objects.get(username=self.user)
        e = Facilities.objects.filter(hostel=userid)
        for i in e:
            if i.title.lower() == title.lower():
                raise forms.ValidationError('Facility with same title is already there')
        return self.cleaned_data

class EditFacilityForm(forms.ModelForm):
    class Meta:
        model = Facilities
        fields = ['title','description','photo']
    def __init__(self, *args, **kwargs):
        self.pk = kwargs.pop('pk', None)
        self.user = kwargs.pop('user',None)
        super(EditFacilityForm, self).__init__(*args, **kwargs)
    def clean(self):
        hostel = Facilities.objects.get(pk=self.pk).hostel
        if str(hostel) != str(self.user):
            raise forms.ValidationError('Invalid Request')
        else:
            title = self.cleaned_data.get('title')
            userid = Hostels.objects.get(username=self.user)
            e = Facilities.objects.filter(hostel=userid)
            for i in e:
                if int(i.pk) != int(self.pk):
                    if i.title.lower() == title.lower():
                        raise forms.ValidationError('Facility with same title is already there')
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
