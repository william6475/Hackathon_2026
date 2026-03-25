from django.contrib.auth import login
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect

import hackathon_app.models
from hackathon_app.models import user_table
# from hackathon_app.models import admin,endUser,Generic_User
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
# Create your views here.

#this function allows the user to view item recommendations
def home(request):
    template = loader.get_template('index.html')
    item_recommendations = ["Temp Value","Temp Value"]
    context = {'temp' : item_recommendations}
    return HttpResponse(template.render(context, request))



"""
Functions require the user to:
 - Front page with login functionality. (DONE)
 - view item recommendations based off taste profile
 - admins can update stock amount
 - auto-stock functionality

Possible additional functions
 - Payment
 - Donations
"""

def register_view(request):
    form = UserCreationForm()
    template = loader.get_template('register.html')
    context = {'form' : form}
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            user_table.objects.create(user_username=username)
            return redirect('home')
    return HttpResponse(template.render(context, request))

"""

def is_user_in_group(user, group_name):
    return user.groups.filter(name=group_name).exists()
# End of temporary views


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    class Meta:
        model = hackathon_app.models.Generic_User
        fields = ( "email", "first_name", "last_name", "password1", "password2")

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user_email = str(form.get_user())
            login(request, form.get_user())
            try:
                student_user = endUser.objects.get(email=user_email)
                return redirect('home')
            except:
                print("No user with matching credentials")
            try:
                admin_user = admin.objects.get(email=user_email)
                return redirect('home')
            except:
                print("No admin with matching credentials")
            if "next" in request.POST:
                return redirect(request.POST.get("next"))
            else:
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, "login_test.html", {"form": form})

"""


def login_page(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = str(form.cleaned_data.get('username'))
            login(request, form.get_user())
            try:
                general_user=user_table.objects.get(username=username)
                return redirect('')
            except:
                print("No user with matching credentials")

            if "next" in request.POST:
                return redirect(request.POST.get("next"))
            else:
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, "login-test.html", {"form": form})