from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
from datetime import *
from djangoapp.models import CustomUser

import json

def JSONserialize(object):
    return serializers.serialize("json",[object])

@csrf_exempt
def index(request):
    #127.0.0.1:8000/test
    ip = request.META.get('REMOTE_ADDR')
    user = User.objects.get(username="kajornsak")

    print(ip)
    #a = CustomUser.objects.get(user_id=1)
    output = JSONserialize(user)
    #output = JSONserialize(a)

    return HttpResponse(output,content_type="application/json")

@csrf_exempt
def login(request):

    datain = request.POST
    if(datain['username'] == "kajornsak" and datain['password']=="016400"):
        response = 200
    else:
        response = 400
    
    dataout = {"status_code" : response}
    dataout = json.dumps(dataout)
    return HttpResponse(dataout,content_type="application/json")