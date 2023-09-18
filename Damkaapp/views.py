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
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

from django.http import JsonResponse
import json
# Create your views here.




# Create your views here.

def index(request):
  

    return render(request, 'index.html')

def resources(request):
  

    return render(request, 'resources.html')
def about(request):
  

    return render(request, 'about.html')
def activities(request):
  

    return render(request, 'activities.html')
def donate(request):
  

    return render(request, 'donate.html')

