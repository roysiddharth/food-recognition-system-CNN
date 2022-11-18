from django import forms
from django.contrib.auth.models import User
from app_1.models import HealthInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','first_name','last_name','email')

class HealthForm(forms.ModelForm):
    class Meta():
        db_table = 'Health_Information'
        model = HealthInfo
        fields = ('dob', 'age', 'gender')
        
