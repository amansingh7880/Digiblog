from django.shortcuts import redirect, render
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate,login ,logout,get_user_model
from django.contrib import messages

User =get_user_model()# Create your views here.

def login_view(request):
   form = LoginForm(request.POST or None)
   if form.is_valid():
      uname = form.cleaned_data.get('username')
      pwd = form.cleaned_data.get('password')
      user = authenticate(request,username=uname, password=pwd)
      if user is not None:
         login(request ,user)
         messages.success(request, 'Login SucessFul')
         return redirect('/')
      else:
         messages.error(request,"Worng Credentitials")
   ctx = {
      'form': form,
      'title':'Login|Digiblog'   
   }
   return render(request, "accounts/login.html", ctx)

def register_view(request):
   form = RegisterForm(request.POST or None)
   if form.is_valid():
      username = form.cleaned_data.get('username')
      email = form.cleaned_data.get('email')
      password = form.cleaned_data.get('password')
      confirmpassword = form.cleaned_data.get('confirmpassword')
      if password== confirmpassword:
         user =User.objects.create_user(username,email,password)
         user.save()
         messages.success(request,'Registration Successful')
         return redirect('/')#redirect to home page
      else:
          messages.success(request,'Password do not match')
   ctx = {'form':form,'title' :'Register|Digiblog'}
   return render(request,"accounts/register.html",ctx)