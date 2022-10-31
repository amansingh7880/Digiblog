import email
from django import forms
from django.contrib.auth.models import User

INVALID_USERNAME=('admin','administarator','root')

#login from
class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(
        widget=forms.PasswordInput
    )
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User .objects.filter(username__iexact=username)
        if not qs.exists():
            raise forms.ValidationError("Invalid Credentials")
        return username

# register form

class RegisterForm(forms.Form):
    username=forms.CharField()
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    confirmpassword=forms.CharField(widget=forms.PasswordInput)

def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User .objects.filter(username__iexact=username)
        if not qs.exists():
            raise forms.ValidationError("User name is Not available")
        if username.lower() in INVALID_USERNAME:
            raise forms.ValidationError("User name is Invalid")
        return username
def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User .objects.filter(username__iexact=email)
        if not qs.exists():
            raise forms.ValidationError("Email is already exists")
        return email