from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate
from newapp.models import *
from django.contrib.admin.widgets import AdminDateWidget

class CreateStudentForm(forms.ModelForm):
    class Meta:
        model = Students
        exclude = ['username', 'current_sem_join_date', 'current_hostel_join_date', 'fee_last_submitted', 'corpus_calculated_uptill', 'corpus', 'room_number', 'branch']
    def __init__(self, *args, **kwargs):
                    self.user_cache = None
                    super(CreateStudentForm, self).__init__(*args, **kwargs)
    def clean(self):
        student_phone_num = self.cleaned_data.get('student_phone_num')
        if len(str(student_phone_num)) == 10:
            pass
        else:
            raise forms.ValidationError('Enter your valid 10 digit phone number')

        distance_from_nsit = self.cleaned_data.get('distance_from_nsit')
        if type(distance_from_nsit) != int:
            raise forms.ValidationError('This field has to be an integer')
        if distance_from_nsit > 0:
            pass
        else:
            raise forms.ValidationError('Enter a valid positive distance from NSIT')            

        parent_phone_num = self.cleaned_data.get('parent_phone_num')
        if len(str(parent_phone_num)) == 10:
            pass
        else:
            raise forms.ValidationError('Enter your parents valid 10 digit phone number')

        zipcode = self.cleaned_data.get('permanent_address_zipcode')

        if len(str(zipcode)) == 6:
            pass
        else:
            raise forms.ValidationError('Enter a valid 6 digit zipcode')

        local_guardian_phone_num = self.cleaned_data.get('local_guardian_phone_num')
        if local_guardian_phone_num == '':
            pass
        else:
            if len(str(local_guardian_phone_num)) != 10:
                raise forms.ValidationError('Enter your local guardians valid 10 digit phone number')
            else:
                pass
        zipcode = self.cleaned_data.get('local_guardian_address_zipcode')
        
        if len(str(zipcode)) == 6:
            pass
        else:
            raise forms.ValidationError('Enter local guardians valid 6 digit zipcode')
        return self.cleaned_data
    def get_user(self):
        return self.user_cache
    
class MakeComplaintForm(forms.ModelForm):
    #code
    class Meta:
        model = Complaints
        fields = ['description']
    
