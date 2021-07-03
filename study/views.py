# Page Redirect , Request Page , Response Page
from django.shortcuts import render, HttpResponse, redirect
# Showing Message alert on Main Page
from django.contrib import messages
# import Tables
from study.models import UserManage, Chapter, Comment
# Login account
from django.contrib.auth import authenticate, login, logout
# Change Password
from django.contrib.auth.forms import PasswordChangeForm
# Gmail Request Add
import smtplib
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
    return render(request, 'index.html')


def start_learn(request, standard):
    context = {'std': standard}
    return render(request, 'start_learn.html', context)


def get_lessions(request, standard, subject):
    lactures = Chapter.objects.filter(
        Q(subject__contains=subject) | Q(standard__contains=standard))
    print(lactures)
    context = {'std': standard, 'sub': subject, 'lactures': lactures}
    return render(request, 'lessions.html', context)


def lacture_details(request, id):
    lacture = Chapter.objects.filter(id=id)
    download = [lacture[0].presentation, lacture[0].notes, lacture[0].video]
    comment = Comment.objects.filter(chapter_id=id)
    return render(request, 'lacture_details.html', context={'lacture': lacture, 'download': download, 'comment': comment})


def add_chapter(request, sub, std):
    if request.method == "POST":
        name = request.POST['name']
        subject = request.POST['subject']
        standard = request.POST['standard']
        try:
            presentation = request.FILES['presentation']
            fs = FileSystemStorage()
            filename1 = fs.save(presentation.name, presentation)

            notes = request.FILES['notes']
            filename2 = fs.save(notes.name, notes)

            video = request.FILES['video']
            filename3 = fs.save(video.name, video)
        except:
            pass

        u = Chapter.objects.create(name=name ,subject=subject , standard=standard , presentation=filename2 , notes=filename2 , video=filename3)
        u.save()
    context = {'sub': sub, 'std': std}
    return render(request, 'add_chapter.html', context)


def comment(request, id):
    if request.method == "POST":
        comment = request.POST['comment']
        c = Comment.objects.create(comment=comment, chapter_id=id)
        c.save()
    return redirect(f'/lacture_details/{id}')


def handleLogin(request):
    if request.method == "POST":
        usrname = request.POST['usrname']
        pswd = request.POST['pswd']
        user = authenticate(username=usrname, password=pswd)
        if user is not None:
            login(request, user)
            return redirect('/')
    return render(request, 'user_login/login.html')


def handleRegister(request):
    if request.method == "POST":
        username = request.POST['usrname']
        password = request.POST['pswd']
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        email = request.POST['email']
        mobile = request.POST['mobile']
        dob = request.POST['dob']
        fieldName = "student"

        try:
            userImg = request.FILES['usrImg']
            fs = FileSystemStorage()
            filename = fs.save(userImg.name, userImg)
            uploaded_file_url = fs.url(filename)
        except:
            pass

        user = UserManage.objects.create_user(username=username, password=password, first_name=first_name,
                                              last_name=last_name, email=email, mobile=mobile, dob=dob, fieldName=fieldName, userImg=userImg)
        user.save()

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
    return render(request, 'user_login/register.html')


def handleLogout(request):
    logout(request)
    return redirect('/')
