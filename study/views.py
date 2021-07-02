# Page Redirect , Request Page , Response Page
from django.shortcuts import render, HttpResponse, redirect
# Showing Message alert on Main Page
from django.contrib import messages
# import Tables
from study.models import UserManage
# Login account
from django.contrib.auth import authenticate, login, logout
# Change Password
from django.contrib.auth.forms import PasswordChangeForm
# Gmail Request Add
import smtplib
# Import json
from django.http import JsonResponse
# For Search Query
from django.db.models import Q
# Store User Image
from django.core.files.storage import FileSystemStorage
# CSRF Token
from django.views.decorators.csrf import csrf_exempt
# Date Time
from django.utils.timezone import datetime
from datetime import date

def index(request):
    return render(request , 'index.html')

def start_learn(request , standard):
    context = {'std':standard}
    return render(request , 'start_learn.html' , context)

def handleLogin(request):
    if request.method == "POST":
        usrname = request.POST['usrname']
        pswd = request.POST['pswd']
        user = authenticate(username=usrname, password=pswd)
        if user is not None:
            login(request, user)
            return redirect('/')
    return render(request , 'user_login/login.html')
    
def handleRegister(request):
    if request.method == "POST":
        username = request.POST['usrname']
        password = request.POST['pswd']
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        email = request.POST['email']
        mobile = request.POST['mobile']
        dob = request.POST['dob']
        fieldName = "Student"

        try:
            userImg = request.FILES['usrImg']
            fs = FileSystemStorage()
            filename = fs.save(userImg.name, userImg)
            uploaded_file_url = fs.url(filename)
        except:
            pass

        user = UserManage.objects.create_user(username=username , password=password , first_name=first_name , last_name=last_name , email=email , mobile=mobile , dob=dob , fieldName=fieldName , userImg=userImg)
        user.save()

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
    return render(request , 'user_login/register.html')
    
def handleLogout(request):
    logout(request)
    return redirect('/')