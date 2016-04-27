from django import forms 
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate
from newapp.models import *
import re
from django.contrib.admin.widgets import AdminDateWidget

class CreateWardenForm(forms.Form):
    userid = forms.CharField(max_length = 254,required = True)
    email = forms.EmailField()
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

class AddBranchForm(forms.ModelForm):
    class Meta:
        model=Branch
        fields = "__all__"
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
            raise forms.ValidationError('This Name Already Exists')
        return name
    def clean_roll_code(self):
        roll_code= self.cleaned_data.get('roll_code')
        roll_code= roll_code.upper()
        b = None
        try:
            b = Branch.objects.get(roll_code=roll_code)
        except ObjectDoesNotExist:
            pass
        if b is not None:
            raise forms.ValidationError('This code Already Exists')
        return roll_code
class EditBranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = "__all__"
    def __init__(self, *args, **kwargs):
        self.pk = kwargs.pop('pk', None)
        super(EditBranchForm, self).__init__(*args, **kwargs)
    def clean(self):
        title = self.cleaned_data.get('title')
        roll_code = self.cleaned_data.get('roll_code')
        name = self.cleaned_data.get('name')
        e = Branch.objects.all()
        for i in e:
            if int(i.pk) != int(self.pk):
                if i.title.upper() == title.upper():
                    raise forms.ValidationError('Branch with same title already exists')
                elif i.name.upper() == name.upper():
                    raise forms.ValidationError('Branch with same Name already exists')
                elif i.roll_code.upper() == roll_code.upper():
                    raise forms.ValidationError('Branch with same Roll Code already exists')
        return self.cleaned_data

class AddNoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        exclude = ['creator','date']


class SearchHostelRoomForm(forms.Form):
    hostel = forms.ModelChoiceField(queryset = Hostels.objects.all())
    room_no = forms.CharField(max_length=10,help_text='Search Room by Room Number, format : AA-111')
    def __init__(self, *args, **kwargs):
        super(SearchHostelRoomForm, self).__init__(*args, **kwargs)
    def clean(self):
        room_no = self.cleaned_data.get('room_no')
        if room_no:
            room_no = room_no.upper()
            if re.match("[A-Z]+-[0-9]+",str(room_no))==None:
                raise forms.ValidationError('Enter Room Number in correct format: AA-111')
        else:
            raise forms.ValidationError('Room Number cannot be empty.')
        return self.cleaned_data

class AddCriminalForm(forms.ModelForm):
    class Meta:
        model = CriminalRecord
        exclude = ['student']
        widgets = {
            'date_of_action':AdminDateWidget(),
        }
class addBankForm(forms.ModelForm):
    class Meta:
        model = Banks
        fields = ['name',]
class EditBankForm(forms.ModelForm):
    class Meta:
        model = Banks
        fields = "__all__"
    def __init__(self, *args, **kwargs):
        self.pk = kwargs.pop('pk', None)
        super(EditBankForm, self).__init__(*args, **kwargs)
    def clean(self):
        ba = Banks.objects.all()
        name = self.cleaned_data.get('name')
        for i in ba:
            if int(i.pk) != int(self.pk):   
                if i.name.upper() == name.upper():
                    raise forms.ValidationError("Error: bank with this name already exists.")
        return self.cleaned_data