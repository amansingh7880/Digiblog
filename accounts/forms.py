from django import form
from django.contrib.auth.models import User
from django.forms import CharField
#login from
class LoginForm(form.Form):
    username=form.CharField()
    password=form.CharField()
    
    def clean_username(self):
        username = self.clean_data.get('username')
        qs = User .objects.filter(username_iexact=username)
        if not qs.exists():
            raise form.ValidationError("Invalid Credentials")
        return username

# register form