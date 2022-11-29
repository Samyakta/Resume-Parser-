from .models import Recruiter,Parser
from django import forms

class ParserForm(forms.ModelForm):
    class Meta:
        model = Parser

        fields = [ 'file']
        widgets = {
            

        }

class RecruiterForm(forms.ModelForm):
    class Meta:
        model = Recruiter

        fields = ['username','firstName','lastName', 'age', 'dob', 'companyName','designationName', 'city', 'contactNumber', 'email', 'password','confirmPassword', 'image']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'firstName': forms.TextInput(attrs={'class': 'form-control'}),
            'lastName': forms.TextInput(attrs={'class': 'form-control'}),
           
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'dob': forms.DateInput(attrs={'class': 'form-control'}),
            'companyName': forms.TextInput(attrs={'class': 'form-control'}),
            'designationName': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'contactNumber': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'confirmPassword': forms.PasswordInput(attrs={'class': 'form-control'}),

        }