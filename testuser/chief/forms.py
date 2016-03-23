from django import forms 
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate
from newapp.models import *
import re

class CreateWardenForm(forms.Form):
    userid = forms.CharField(max_length = 254,required = True)
    password = forms.CharField(widget = forms.PasswordInput,required = True)
    retype_password = forms.CharField(widget = forms.PasswordInput,required = True)
    def __init__(self, *args, **kwargs):
        self.user_cache = None
        super(CreateWardenForm, self).__init__(*args, **kwargs)
    def clean_userid(self):
        userid = self.cleaned_data.get('userid')
        userid = userid.lower()
        if not re.match("[bg]h[0-9]*warden",userid):
            raise forms.ValidationError('Not a correct format for this field')
        h = None
        m = None
        try:
            h = Hostels.objects.get(username=userid)
            m = MyUser.objects.get(userid=userid)
        except ObjectDoesNotExist:
            pass
        if h is not None or m is not None:
        	raise forms.ValidationError('User Alredy Exists')
        return userid
    def clean_retype_password(self):
        p = self.cleaned_data.get('password')
        q = self.cleaned_data.get('retype_password')
        if not q==p:
            raise forms.ValidationError('Passwords do not match')
        return q
    def get_user(self):
        return self.user_cache

class AddBranchForm(forms.Form):
    title = forms.CharField(max_length = 5)
    name = forms.CharField(max_length = 100)
    Roll_Code = forms.CharField(max_length = 5,required = True)
    def __init__(self, *args, **kwargs):
        super(AddBranchForm, self).__init__(*args, **kwargs)
    def clean_title(self):
        title = self.cleaned_data.get('title')
        title = title.upper()
        b = None
        try:
            b = Branch.objects.get(title=title)
        except ObjectDoesNotExist:
            pass
        if b is not None:
            raise forms.ValidationError('Branch Already Exists')
        return title
    
    def clean_name(self):
        
        name = self.cleaned_data.get('name')
        name = name.upper()
        b = None
        try:
            b = Branch.objects.get(name=name)
        except ObjectDoesNotExist:
            pass
        if b is not None:
            raise forms.ValidationError('This code Already Exists')
        return name
    def clean_Roll_Code(self):
        
        Roll_Code= self.cleaned_data.get('Roll_Code')
        Roll_Code= Roll_Code.upper()
        b = None
        try:
            b = Branch.objects.get(roll_code=Roll_Code)
        except ObjectDoesNotExist:
            pass
        if b is not None:
            raise forms.ValidationError('This code Already Exists')
        return Roll_Code
