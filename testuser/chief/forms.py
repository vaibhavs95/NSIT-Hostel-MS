from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate
from newapp.models import *
import re

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
    
    def clean_userid(self):
        userid = self.cleaned_data.get('userid')
        if not re.match("[bh]h[0-9]*warden",userid):
            raise forms.ValidationError('Not a correct format for this field')
        return self.cleaned_data
    
    def get_user(self):
        return self.user_cache