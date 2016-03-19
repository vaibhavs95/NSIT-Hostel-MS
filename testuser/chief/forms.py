from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate
from newapp.models import *

class CreateWardenForm(forms.Form):
    userid = forms.CharField(max_length = 254)
    password = forms.CharField(widget = forms.PasswordInput)
    retype_password = forms.CharField(widget = forms.PasswordInput)
    def __init__(self, *args, **kwargs):
        self.user_cache = None
        super(CreateWardenForm, self).__init__(*args, **kwargs)
    def clean(self):
        userid = self.cleaned_data.get('userid')
        password = self.cleaned_data.get('password')
        h = None
        m = None
        try:
        	h = Hostels.objects.get(username=userid)
        	m = MyUser.objects.get(userid=userid)
        except ObjectDoesNotExist:
        	pass
        if h is not None or m is not None:
        	raise forms.ValidationError('User Alredy Exists')
        return self.cleaned_data
    def clean_retype_password(self):
        p = self.cleaned_data.get('password')
        q = self.cleaned_data.get('retype_password')
        if not q==p:
            raise forms.ValidationError('Passwords do not match')
    def get_user(self):
        return self.user_cache

class AddBranchForm(forms.Form):
    title = forms.CharField(max_length = 5)
    name = forms.CharField(max_length = 100)
    def __init__(self, *args, **kwargs):
        super(AddBranchForm, self).__init__(*args, **kwargs)
    def clean(self):
        title = self.cleaned_data.get('title')
        name = self.cleaned_data.get('name')
        title = title.upper()
        b = None
        try:
            b = Branch.objects.get(title=title)
        except ObjectDoesNotExist:
            pass
        if b is not None:
            raise forms.ValidationError('Branch Already Exists')
        return self.cleaned_data