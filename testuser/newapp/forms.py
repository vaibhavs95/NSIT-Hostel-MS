from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate
from .models import *
class LoginForm(forms.Form):
    userid = forms.CharField(max_length = 254,required = True)
    password = forms.CharField(widget = forms.PasswordInput,required=True)

    def __init__(self, *args, **kwargs):
        self.user_cache = None
        super(LoginForm, self).__init__(*args, **kwargs)
    def clean_userid(self):
        user = self.cleaned_data.get('userid') 
        if user is None:
            raise forms.ValidationError("This Field is required")
        return user
    def clean_password(self):
        password = self.cleaned_data.get('password') 
        if password is None:
            raise forms.ValidationError("This Field is required")
        return password
    def clean(self):
        userid = self.cleaned_data.get('userid')
        password = self.cleaned_data.get('password')
        self.user_cache = authenticate(userid = userid, password = password)
        if self.user_cache is None:
            raise forms.ValidationError('Invalid Username or Password')
        elif not self.user_cache.is_active:
            raise forms.ValidationError('This account is inactive')
        return self.cleaned_data
    def get_user(self):
        return self.user_cache
    
    
class ForgetForm(forms.Form):
    UserId = forms.CharField(max_length = 50,required = True)

class ResetPasswordForm(forms.Form):
    #code
    new_Password = forms.CharField(widget = forms.PasswordInput,required=True)
    retype_Password = forms.CharField(widget = forms.PasswordInput,required=True)
    
    def __init__(self, *args, **kwargs):
        self.user_cache = None
        super(ResetPasswordForm, self).__init__(*args, **kwargs)
        
    def clean(self):
        pas = self.cleaned_data.get('new_Password')
        repas = self.cleaned_data.get('retype_Password')
        if pas != repas:
            raise ValidationError('Passwords did not match')
        return self.cleaned_data
