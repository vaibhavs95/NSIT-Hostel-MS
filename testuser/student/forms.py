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
    
class MakeComplaintForm(forms.ModelForm):
    #code
    class Meta:
        model = Complaints
        exclude = ['lodgers_roll_no','hostel','date_of_complaint','closed']
    
