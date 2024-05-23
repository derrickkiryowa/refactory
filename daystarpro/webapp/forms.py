from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django import forms
from django.forms.widgets import PasswordInput, TextInput
from .models import Baby, Sitter, Doll, Procurement, AssignProcurement, DollSales

#create or register user

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

 #login a user

class LoginForm(AuthenticationForm): 
    username = forms.CharField(widget=TextInput())     
    password = forms.CharField(widget=PasswordInput())     


class AddBabyForm(forms.ModelForm):
    class Meta:
        model = Baby
        fields = ['first_name', 'last_name', 'age', 'gender', 'parents_name', 'drop_off', 'pickedby', 'periodofstay', 'location', 'time_out']


class AddSitterForm(forms.ModelForm):
    class Meta:
        model = Sitter
        fields = ['name', 'dob', 'gender', 'next_of_kin', 'NIN', 'recommender_name', 'level_of_education', 'sitter_number', 'contacts']

class DollForm(forms.ModelForm):   
    class Meta:
        model = Doll
        fields = '__all__'

class ProcurementForm(forms.ModelForm):
    class Meta:
        model = Procurement
        fields = '__all__'

class AssignProcurementForm(forms.ModelForm):
    class Meta:
        model = AssignProcurement
        fields = '__all__'

class DollSalesForm(forms.ModelForm):
    class Meta:
        model = DollSales
        fields = '__all__'          
