from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm,ProfileUpdateForm,UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login
from .models import Profile
# Create your views here.
def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST) #creates an inst with POST data
        if form.is_valid():
            user=form.save()
            username=form.cleaned_data.get('username') #cleaned_data gets it as py dict
            messages.success(request,f'Account Created sucessfully for {username} but profile incomplete') #f= formatted string in py
            request.session['username']=username
            return redirect('content-home')
    else:
        form=UserRegisterForm() #creates a blank form
    return render(request,'author/register.html',{'form':form})
#to restrict back button after logout

@login_required
def profile(request):
    if request.method=='POST':
        u_form=UserUpdateForm(request.POST,instance=request.user)
        a_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and a_form.is_valid():
            u_form.save()
            a_form.save()
            username=u_form.cleaned_data.get('username')
            messages.success(request,f'Profile Updated sucessfully for {username}')
            return redirect('profile')
    else:
        u_form=UserUpdateForm(instance=request.user)
        a_form=ProfileUpdateForm(instance=request.user.profile)
    context={
        'u_form':u_form,
        'a_form':a_form,
    }
    return render(request,'author/profile.html',context)