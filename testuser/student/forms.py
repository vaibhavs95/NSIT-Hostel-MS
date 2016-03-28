from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate
from newapp.models import *

class CreateStudentForm(forms.Form):
    name = forms.CharField(max_length = 254)
    date_of_birth = forms.DateTimeField()
    distance_from_nsit = forms.IntegerField()
    gender = forms.ChoiceField(choices = GENDER_CHOICES, required = True)
    college_category = forms.ChoiceField(choices = COLLEGE_CAT, required = True) 
    blood_group = forms.ChoiceField(choices = BLOOD_GROUP, required = True) # A+, A-, B+, B-, AB+, AB-, O-, O+
    student_phone_num = forms.IntegerField() # 10 digits
    student_email = forms.EmailField()
    student_optional_phone_num = forms.IntegerField(required = False)
    father_name = forms.CharField(max_length = 254)
    mother_name = forms.CharField(max_length = 254)
    parent_email = forms.EmailField()
    parent_phone_num = forms.IntegerField()
    parent_optional_phone_num = forms.IntegerField(required = False)
    permanent_address = forms.CharField(max_length = 254)
    permanent_address_zipcode = forms.IntegerField()
    local_guardian_name = forms.CharField(max_length = 254)
    local_guardian_address = forms.CharField(max_length = 254)
    local_guardian_address_zipcode = forms.IntegerField()
    local_guardian_phone_num = forms.IntegerField()
    local_guardian_optional_phone_num = forms.IntegerField(required = False)
    local_guardian_email = forms.EmailField(max_length = 254)
    # password = forms.CharField(widget = forms.PasswordInput)
    # retype_password = forms.CharField(widget = forms.PasswordInput)
    def __init__(self, *args, **kwargs):
                    self.user_cache = None
                    super(CreateStudentForm, self).__init__(*args, **kwargs)
    def clean(self):
    	student_phone_num = self.cleaned_data.get('student_phone_num')
    	parent_phone_num = self.cleaned_data.get('parent_phone_num')
    	local_guardian_phone_num = self.cleaned_data.get('local_guardian_phone_num')
    	if len(str(student_phone_num)) == 10 and len(str(parent_phone_num)) == 10 and len(str(local_guardian_phone_num)) == 10:
    		pass
    	else:
    		raise forms.ValidationError('Enter a valid 10 digit phone number')
    	blood_group = self.cleaned_data.get('blood_group')
    	return self.cleaned_data

    def get_user(self):
        return self.user_cache