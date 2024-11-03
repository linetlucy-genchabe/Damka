from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.conf import settings
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.templatetags.static import static
# from django.shortcuts import render, redirect, render_to_response, HttpResponseRedirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
import datetime as dt
from .models import *
from .forms import *
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

from django.http import JsonResponse
import json


def index(request):
  

    return render(request, 'index.html')

def resources(request):
  

    return render(request, 'resources.html')
def about(request):
  

    return render(request, 'about.html')
def activities(request):
    activities = Activity.objects.all()
  
    
    return render(request,  'activities.html', {'activities':activities})


def donate(request):
  

    return render(request, 'donate.html')
def events(request):
    events = Event.objects.all()

    return render(request, 'events.html', {'events':events})
def careers(request):
  

    return render(request, 'vacancies.html')


def user_login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']  
        
        user = authenticate (request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"Welcome , you are now logged in")
            return redirect ("index")
        else:
            messages.error(request,'Username or password not correct')
            return redirect('login')
        
    return render(request, 'login.html' )


@login_required(login_url='/login/')
def new_activity(request):
    current_user = request.user
    profile = request.user.profile
   

    if request.method == 'POST':
        form = NewActivityForm(request.POST, request.FILES)
        if form.is_valid():
            activity = form.save(commit=False)
            activity.Author = current_user
            activity.author_profile = profile

            activity.save()
        return redirect('index')

    else:
        form = NewActivityForm()
    return render(request, 'newactivity.html', {"form": form})


@login_required(login_url='/login/')
def new_event(request):
    current_user = request.user
    profile = request.user.profile
   

    if request.method == 'POST':
        form1 = NewEventForm(request.POST, request.FILES)
        if form1.is_valid():
            event = form1.save(commit=False)
            event.Author = current_user
            event.author_profile = profile

            event.save()
        return redirect('index')

    else:
        form1 = NewEventForm()
    return render(request, 'newevent.html', {"form1": form1})

 
def signout(request):
    logout(request)
    messages.success(request,"You have logged out")
           
    return redirect("/")