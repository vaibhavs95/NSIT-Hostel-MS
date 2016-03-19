from django import forms
from django.forms import ModelForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate
from newapp.models import *
import re

class EditWardenProfileForm(forms.ModelForm):
    class Meta:
        model = Hostels
        fields = ['name','phone','email','landline','department','portfolio']
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(EditWardenProfileForm, self).__init__(*args, **kwargs)
    def clean(self):
        name = self.cleaned_data.get('name')
        phone = self.cleaned_data.get('phone')
        landline = self.cleaned_data.get('landline')
        email = self.cleaned_data.get('email')
        department = self.cleaned_data.get('department')
        portfolio = self.cleaned_data.get('portfolio')
        if name and phone and landline and email and department and portfolio:
            name = name.title()
            if len(phone) > 13:
                raise forms.ValidationError('Enter Correct Phone Number')
            if len(landline) > 11:
                raise forms.ValidationError('Enter Correct Landline Number')
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
                print('inside if')
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
                print (s)
                print(u)
                if s is not None or u is not None:
                    raise forms.ValidationError('Student Alredy Exists')
                e = Students.objects.all()
                for i in e:
                    if i.student_email == student_email:
                        raise forms.ValidationError('Email is already registered')
            else:
                raise forms.ValidationError('Incorrect format of username.(Correct format: 111-CO-15)')
        return self.cleaned_data
