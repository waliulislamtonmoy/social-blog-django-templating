from django.shortcuts import render
from django.shortcuts import redirect,HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,PasswordChangeForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

from django.contrib.auth import logout
from django.shortcuts import HttpResponsePermanentRedirect
from django.urls import reverse
# Create your views here.

from App_Account.forms import SignUpForm,ProfileChangeForm



def sign_up(request):
    form=SignUpForm()
    if request.method=="POST":
        form=SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("/login")
    return render(request,'App_Account/Register.html',{'form':form})


def sign_in(request):
    form=AuthenticationForm()
    if request.method=="POST":
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return  render(request,"App_Blog/Home.html")
    return render(request,'App_Account/Login.html',{'form':form})
            
@login_required           
def user_logout(request):
    logout(request)
    return HttpResponsePermanentRedirect(reverse("login"))

@login_required
def Profile(request):
    return render(request,"App_Account/Profile.html")

@login_required
def user_change(request):
    user=request.user
    form=ProfileChangeForm(instance=user)
    if request.method=="POST":
        form=ProfileChangeForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            form=ProfileChangeForm(instance=user)
            return redirect("/profile")
    return render(request,'App_Account/Profilechange.html',context={"form":form})
            
@login_required
def password_change(request):
    user=request.user 
    form=PasswordChangeForm(user)
    if request.method=="POST":
         form=PasswordChangeForm(user,data=request.POST)
         if form.is_valid():
             form.save()
             
    return render(request,'App_Account/passchange.html',context={"form":form})
    