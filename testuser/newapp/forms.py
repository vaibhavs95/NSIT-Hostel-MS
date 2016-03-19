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

    def clean(self):
        userid = self.cleaned_data.get('userid')
        password = self.cleaned_data.get('password')
<<<<<<< HEAD
        if userid is None or password is None:
            raise forms.ValidationError('Fields cannot be blank')
        if userid and password:
            self.user_cache = authenticate(userid = userid, password = password)
            if self.user_cache is None:
                raise forms.ValidationError('Please enter a correct username and password')
            elif not self.user_cache.is_active:
                raise forms.ValidationError('This account is inactive')
=======
        self.user_cache = authenticate(userid = userid, password = password)
        if self.user_cache is None:
            raise forms.ValidationError('Please enter a correct username and password')
        elif not self.user_cache.is_active:
            raise forms.ValidationError('This account is inactive')
>>>>>>> 6f7c0af2dc6fb34ebfe38da446ca9d81fec8e224
        return self.cleaned_data
    def get_user(self):
        return self.user_cache
    
    
