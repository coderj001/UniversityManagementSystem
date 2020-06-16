import datetime
import os
# Calling inbuilt django models
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from managementApp.EmailBackEnd import EmailBackEnd
from UniversityManagementSystem import settings

# To Demo Page
def showDemoPage(req):
    return render(req,"demo.html")

# To Render Login Page
def ShowLoginPage(req):
    return render(req,"login_page.html")

# To Auth the User via email and password
def doLogin(req):
    if req.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user=EmailBackEnd.authenticate(req,username=req.POST.get("email"),password=req.POST.get("password"))
        if user!=None:
            login(req,user)
            if user.user_type=="1":
                return HttpResponseRedirect('/admin_home')
            elif user.user_type=="2":
                return HttpResponseRedirect(reverse("staff_home"))
            else:
                return HttpResponseRedirect(reverse("student_home"))
        else:
            messages.error(req,"Invalid Login Details")
            return HttpResponseRedirect("/")

# For Demo Usage
def GetUserDetails(req):
    if req.user!=None:
        return HttpResponse("User : "+req.user.email+" usertype : "+str(req.user.user_type))
    else:
        return HttpResponse("Please Login First")

# To Logout User
def logout_user(req):
    logout(req)
    return HttpResponseRedirect("/")
