from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
# Create your views here.
from djangoapp.models import Person
from djangoapp.models import User

import json

def JSONserialize(object):
    return serializers.serialize("json",[object])

@csrf_exempt
def index(request):


    a = User.objects.get(user_id=1)

    output = JSONserialize(a)

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