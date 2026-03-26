from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, redirect
import hackathon_app.models
from hackathon_app.models import user_table, sales, products_list
# from hackathon_app.models import admin,endUser,Generic_User
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
# Create your views here.

#this function allows the user to view item recommendations
@login_required(login_url="/login/")
def home(request):
    template = loader.get_template('index.html')
    item_recommendations = ["Temp Value","Temp Value"]
    context = {'temp' : item_recommendations}
    return HttpResponse(template.render(context, request))

def catalogue(request):
    template = loader.get_template('new-catalogue.html')
    elec_1_query = sales.objects.raw("Select * from main.sales_data where product_label = 'P0001'")
    elec_1 = elec_1_query[1]
    elec_1_name = products_list.objects.get(product_label='P0001').product_description
    elec_2_query = sales.objects.raw("Select * from main.sales_data where product_label = 'P0004'")
    elec_2 = elec_2_query[1]
    elec_2_name = products_list.objects.get(product_label='P0004').product_description
    elec_3_query = sales.objects.raw("Select * from main.sales_data where product_label = 'P0008'")
    elec_3 = elec_3_query[1]
    elec_3_name = products_list.objects.get(product_label='P0008').product_description
    cloth_1_query = sales.objects.raw("Select * from main.sales_data where product_label = 'P0002'")
    clot_1_name = products_list.objects.get(product_label='P0002').product_description
    clot_1=cloth_1_query[1]
    cloth_2_query = sales.objects.raw("Select * from main.sales_data where product_label = 'P0003'")
    clot_2_name = products_list.objects.get(product_label='P0003').product_description
    clot_2 = cloth_2_query[1]
    cloth_3_query = sales.objects.raw("Select * from main.sales_data where product_label = 'P0009'")
    clot_3_name = products_list.objects.get(product_label='P0009').product_description
    clot_3 = cloth_3_query[1]
    groc_1_query = sales.objects.raw("Select * from main.sales_data where product_label = 'P0005'")
    groc_1_name = products_list.objects.get(product_label='P0005').product_description
    groc_1 = groc_1_query[1]
    groc_2_query = sales.objects.raw("Select * from main.sales_data where product_label = 'P0012'")
    groc_2_name = products_list.objects.get(product_label='P0007').product_description
    groc_2 = groc_2_query[1]
    groc_3_query = sales.objects.raw("Select * from main.sales_data where product_label = 'P0012'")
    groc_3_name = products_list.objects.get(product_label='P0012').product_description
    groc_3 = groc_3_query[1]
    groc_4_query = sales.objects.raw("Select * from main.sales_data where product_label = 'P0014'")
    groc_4_name = products_list.objects.get(product_label='P0014').product_description
    groc_4 = groc_4_query[1]
    groc_5_query = sales.objects.raw("Select * from main.sales_data where product_label = 'P0016'")
    groc_5_name = products_list.objects.get(product_label='P0016').product_description
    groc_5 = groc_5_query[1]
    groc_6_query = sales.objects.raw("Select * from main.sales_data where product_label = 'P0018'")
    groc_6_name = products_list.objects.get(product_label='P0018').product_description
    groc_6 = groc_6_query[1]
    toys_1_name = "temp"
    toys_1 = ["temp"]
    toys_2_name = "temp"
    toys_2 = ["temp"]
    furn_1_name = "temp"
    furn_1 = ["temp"]
    furn_2_name = "temp"
    furn_2 = ["temp"]


    # This function runs the forecast. It is functional and returns a decimal value between 0 and 1
    # Use the prediction context variable
    #elec_1_forecast = predictions.get_demand_predictions(prediction_context)

    item_recommendations = ["Temp Value","Temp Value"]
    context = {
        'elec_1' : elec_1,
        'elec_1_name' : elec_1_name,
        'elec_2': elec_2,
        'elec_2_name': elec_2_name,
        'elec_3': elec_3,
        'elec_3_name': elec_3_name,

    }
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


@login_required(login_url="/login/")
def logout_page(request):
    logout(request)
    return HttpResponseRedirect("/login/")