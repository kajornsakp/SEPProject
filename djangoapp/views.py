from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
from datetime import *
from djangoapp.models import *
import djangoapp.Separator as Sp
import json

def JSONserialize(object):
    return serializers.serialize("json",[object])

@csrf_exempt
def index(request):

    #127.0.0.1:8000/test
    ip = request.META.get('REMOTE_ADDR')
    #user = User.objects.get(username="kajornsak")

    print(ip)
    #a = CustomUser.objects.get(user_id=1)
    #output = JSONserialize(user)
    #output = JSONserialize(a)


    #reminder = Reminder(user_id="123456",user_remindnote="meeting at IC04",user_adddate=datetime.now().date(),user_reminddate=datetime.now().date(),user_remindtime=datetime.now().strftime('%H:%M:%S'))
    #reminder.save()
    output = ip
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

@csrf_exempt
def reminder(request):
    if(request.method == "GET"):
        dataout = ""
        if 'userid' in request.GET:
            userid = request.GET['userid']
            remind = Reminder.objects.filter(user_id="123456")
            jsonout = serializers.serialize('json', remind)
            return HttpResponse(jsonout,content_type="application/json")
        else:
            dataout += 'no user id'
            dataout = json.dumps(dataout)
            return HttpResponse(dataout, content_type="application/json")

    elif(request.method == "POST"):
        datain = request.POST
        userid = datain['userid']
        remindnote = datain['remindnote']
        adddate = datain['adddate']
        reminddate = datain['reminddate']
        remindtime = datain['remindtime']

        reminder = Reminder(user_id=userid,user_remindnote=remindnote,user_adddate=adddate,user_reminddate=reminddate,user_remindtime=remindtime)
        reminder.save()

        dataout = {"status_code":200}
        jsonout = json.dumps(dataout)
        return HttpResponse(jsonout,content_type="application/json")


def calendar(request):
    dataout = ""
    if 'userid' in request.GET:
        userid = request.GET['userid']
        dataout += "calendar for %s" % (userid)

    else:
        dataout += 'no user id'
    dataout = json.dumps(dataout)
    return HttpResponse(dataout, content_type="application/json")

def note(request):
    dataout = ""
    if 'userid' in request.GET:
        userid = request.GET['userid']
        dataout += "note for %s" % (userid)

    else:
        dataout += 'no user id'
    dataout = json.dumps(dataout)
    return HttpResponse(dataout, content_type="application/json")

def hardware(request):
    dataout = ""
    if 'userid' in request.GET:
        userid = request.GET['userid']
        dataout += "hardware for %s" % (userid)

    else:
        dataout += 'no user id'
    dataout = json.dumps(dataout)
    return HttpResponse(dataout, content_type="application/json")
