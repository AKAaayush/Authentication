from django.shortcuts import render, HttpResponse, redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect
# from django.contrib.auth.forms  import UserCreationForm
from accounts.form import (
     RegistrationForm, 
     EditProfileForm
     
)
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
# Create your views here.
# @login_required
# def home(request):
#     name="Aayush shrestha"
#     number=5


#     ar = {"myName":name, "numbers":number*name}
#     return render(request,'accounts/home.html',ar)

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account')
    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request,'accounts/reg_form.html', args)

# def register(request):
#     form = UserCreationForm(request.POST or None)
#     if request.method == 'POST':
#      if form.is_valid():
#         form.save()
#         return HttpResponseRedirect('account/')

#     else:
#         return render(
#             'accounts/reg_form.html', {'form': form},context=RequestContext(request))
@login_required       
def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user

    args = {'user': user}
    return render(request,'accounts/profile.html', args)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/account/profile')

    else:
        form = EditProfileForm(instance=request.user)
        args = {'form':form}
        return render(request,'accounts/edit_profile.html', args)
        
@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('/account/profile')
        else:
            return redirect('/account/change-password')

    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form':form}
        return render(request,'accounts/change_password.html', args)