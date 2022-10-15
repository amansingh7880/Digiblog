from email import message
from os import uname
from pyexpat.errors import messages
from sre_constants import SUCCESS
from django.shortcuts import redirect, render
from .forms import LoginForm
from django.contrib.auth import authenticate,login
# Create your views here.
def login_view(request):
     form = LoginForm()
     if request.method == 'POST':
         form = LoginForm(request,form)
         uname = form.clean_data.get('username')
         pwd = form.clean_data.get('password')
         user = authenticate(request,username=uname, password=pwd)
         if user is not None:
            login(request ,user)
            messages.success(request, 'Login SucessFul')
            redirect('/')
         else:
            messages.error(request,"Worng Credentitials")
            ctx = {
             'form': form,
             'title':'Login|Digilog'   
    }
            return render(request, "account/login.html", ctx)
