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
from djangoapp.QueryHandler import QueryHandler
import json
import nltk

@csrf_exempt
def query(request):
    if(request.method == "POST"):

        datain = request.POST
        userid = datain['userid']
        querystring = datain['query']
        query = QueryHandler(userid)
        responsestring = query.classify(querystring)
        history = History(user_id=userid,user_querystring=querystring,user_responsestring=responsestring)
        history.save()


        dataout = {'status_code':200,'query':querystring,'response':responsestring}
        jsonout = json.dumps(dataout)

        return HttpResponse(jsonout,content_type="application/json")


@csrf_exempt
def history(request):
    if(request.method == "GET"):
        userid = request.GET['userid']
        history = History.objects.filter(user_id=userid)
        jsonout = serializers.serialize('json',history)
        return HttpResponse(jsonout,content_type="application/json")


@csrf_exempt
def login(request):

    if(request.method == "POST"):
        datain = request.POST
        username = datain['username']
        password = datain['password']
        userexist = User.objects.filter(username=username).exists()

        if(userexist == False):
            response = 404
            detail = "user not found"
            dataout = {"status_code": response, "status_detail": detail}
        else:

            user = User.objects.get(username=username)
            if(user.password == password):
                customeuser = CustomUser.objects.get(user_user=user)
                userid = customeuser.user_id
                response = 200
                detail = "success"
                dataout = {"status_code": response, "status_detail": detail, "userid": userid}

            else:
                response = 404
                detail = "user and password does not match"
                dataout = {"status_code": response, "status_detail": detail}


        dataout = json.dumps(dataout)
        return HttpResponse(dataout,content_type="application/json")


@csrf_exempt
def register(request):
    if(request.method == "POST"):
        datain = request.POST
        username = datain['username']
        password = datain['password']
        if(User.objects.filter(username=username).exists()):
            dataout = {'status_code':400,'status_detail':"username is already in used"}
            jsonout = json.dumps(dataout)
            return HttpResponse(jsonout,content_type="application/json")
        else:
            userid = str(CustomUser.objects.all().count())
            user = User(username=username,password=password)
            user.save()
            customuser = CustomUser(user_user=user,user_id=userid,user_type="user")
            customuser.save()
            dataout = {'status_code':200,'userid':userid}
            jsonout = json.dumps(dataout)
            return HttpResponse(jsonout,content_type="application/json")



#get,add reminder
@csrf_exempt
def reminder(request):
    if(request.method == "GET"):
        if 'userid' in request.GET:
            userid = request.GET['userid']
            remind = Reminder.objects.filter(user_id=userid)
            jsonout = serializers.serialize('json', remind)
            return HttpResponse(jsonout,content_type="application/json")
        else:
            dataout = {"status_code":404,"status_detail":"need user id"}
            dataout = json.dumps(dataout)
            return HttpResponse(dataout, content_type="application/json")

    elif(request.method == "POST" and request.POST):
        datain = request.POST
        userid = datain['userid']
        remindnote = datain['remindnote']
        adddate = datetime.strptime(datain['adddate'],'%Y-%m-%d').date()
        reminddate = datetime.strptime(datain['reminddate'],"%Y-%m-%d").date()
        remindtime = datetime.strptime(datain['remindtime'],"%H:%M:%S").time()
        reminder = Reminder(user_id=userid,user_remindnote=remindnote,user_adddate=adddate,user_reminddate=reminddate,user_remindtime=remindtime)

        reminder.save()

        dataout = {"status_code":200,"reminderobject":json.loads(serializers.serialize('json',[reminder]))}
        jsonout = json.dumps(dataout)
        return HttpResponse(jsonout,content_type="application/json")

#delete reminder
@csrf_exempt
def deletereminder(request):
    if(request.method == "POST"):
        datain = request.POST
        userid = datain['userid']
        reminderid = datain['reminderid']
        reminder = Reminder.objects.get(pk=reminderid)
        if(reminder.user_id==userid):
            reminder.delete()
            status_code = 200
        else:
            status_code = 400

        dataout = {"status_code":status_code}
        jsonout = json.dumps(dataout)
        return HttpResponse(jsonout,content_type="application/json")


#updatereminder
@csrf_exempt
def updatereminder(request):
    if(request.method == "POST"):
        datain = request.POST
        reminderid = datain['reminderid']
        userid = datain['userid']
        remindnote = datain['remindnote']
        adddate = datetime.strptime(datain['adddate'], '%Y-%m-%d').date()
        reminddate = datetime.strptime(datain['reminddate'], "%Y-%m-%d").date()
        remindtime = datetime.strptime(datain['remindtime'], "%H:%M:%S").time()
        reminder = Reminder.objects.get(pk=reminderid)
        if(reminder.user_id == userid):
            reminder.user_remindnote = remindnote
            reminder.user_adddate = adddate
            reminder.user_reminddate = reminddate
            reminder.user_remindtime = remindtime
            reminder.save()
            status_code = 200
            reminderobject = json.loads(serializers.serialize('json',[reminder]))
        else:
            status_code = 400
            reminderobject = "nullobject"

        dataout = {"status_code":status_code,"reminderobject":reminderobject}
        jsonout = json.dumps(dataout)
        return HttpResponse(jsonout,content_type="application/json")

@csrf_exempt
def calendar(request):
    if request.method == "GET":
        if('userid' in request.GET):
            userid = request.GET['userid']
            calendar = Calendar.objects.filter(user_id=userid)
            calendarobject = json.loads(serializers.serialize('json',calendar))
            status_code = 200
            dataout = {'status_code':status_code,'calendarobject':calendarobject}
            jsonout = json.dumps(dataout)
            return HttpResponse(jsonout,content_type='application/json')

    elif(request.method == "POST"):
        datain = request.POST
        userid = datain['userid']
        userevent = datain['userevent']
        userdate = datetime.strptime(datain['userdate'], "%Y-%m-%d").date()
        calendar = Calendar(user_id=userid,user_event=userevent,user_date=userdate)
        calendar.save()
        calendarobject = json.loads(serializers.serialize('json',[calendar]))
        status_code = 200
        dataout = {'status_code':status_code,'calendarobject':calendarobject}
        jsonout = json.dumps(dataout)
        return HttpResponse(jsonout, content_type="application/json")

@csrf_exempt
def updatecalendar(request):
    if(request.method == "POST"):
        datain = request.POST
        userid = datain['userid']
        calendarid = datain['calendarid']
        userevent = datain['userevent']
        userdate = datetime.strptime(datain['userdate'], "%Y-%m-%d").date()
        calendar = Calendar.objects.get(pk=calendarid)
        if(calendar.user_id == userid):
            calendar.user_event = userevent
            calendar.user_date = userdate
            calendar.save()
            calendarobject = json.loads(serializers.serialize('json',[calendar]))
            status_code = 200
            dataout = {'status_code':status_code,'calendarobject':calendarobject}
            jsonout = json.dumps(dataout)
            return HttpResponse(jsonout,content_type="application/json")



@csrf_exempt
def deletecalendar(request):
    if(request.method == "POST"):
        datain = request.POST
        userid = datain['userid']
        calendarid = datain['calendarid']
        calendar = Calendar.objects.get(pk=calendarid)
        if(calendar.user_id == userid):
            calendar.delete()
            status_code = 200
        else:
            status_code = 400
        dataout = {'status_code':status_code}
        jsonout = json.dumps(dataout)
        return HttpResponse(jsonout,content_type="application/json")




#get,add note
@csrf_exempt
def note(request):
    dataout = ""
    if(request.method == "GET"):
        if 'userid' in request.GET:
            userid = request.GET['userid']
            note = Note.objects.filter(user_id=userid)
            jsonout = serializers.serialize('json',note)
            return HttpResponse(jsonout,content_type="application/json")

        else:
            dataout += 'no user id'
            dataout = json.dumps(dataout)
            return HttpResponse(dataout, content_type="application/json")

    elif(request.method == "POST"):
        datain = request.POST
        userid = datain['userid']
        usernoteheader = datain['usernoteheader']
        usernote = datain['usernote']
        notedate = datetime.strptime(datain['notedate'], "%Y-%m-%d").date()
        notetime = datetime.strptime(datain['notetime'], "%H:%M:%S").time()
        note = Note(user_id=userid,user_noteheader=usernoteheader,user_note=usernote,note_date=notedate,note_time=notetime)
        note.save()

        dataout = {"status_code":200,"noteobject":json.loads(serializers.serialize('json',[note]))}
        jsonout = json.dumps(dataout)
        return HttpResponse(jsonout,content_type="application/json")

#deletenote
@csrf_exempt
def deletenote(request):
    if (request.method == "POST"):
        datain = request.POST
        userid = datain['userid']
        noteid = datain['noteid']
        print("noteid " + noteid)
        note = Note.objects.get(pk=noteid)

        if(note.user_id == userid):
            note.delete()
            status_code = 200
        else:
            status_code = 400

        dataout = {"status_code":status_code}
        jsonout = json.dumps(dataout)
        return HttpResponse(jsonout,content_type="application/json")

#updatenote
@csrf_exempt
def updatenote(request):
    if(request.method == "POST"):
        datain = request.POST
        userid = datain['userid']
        noteid = datain['noteid']
        note = Note.objects.get(pk=noteid)
        if(note.user_id == userid):
            usernoteheader = datain['usernoteheader']
            usernote = datain['usernote']
            notedate = datetime.strptime(datain['notedate'], "%Y-%m-%d").date()
            notetime = datetime.strptime(datain['notetime'], "%H:%M:%S").time()

            note.user_noteheader = usernoteheader
            note.user_note = usernote
            note.user_notedate = notedate
            note.user_notetime = notetime
            note.save()
            status_code = 200
            dataout = {'status_code':status_code,'noteobject':json.loads(serializers.serialize('json',[note]))}
            jsonout = json.dumps(dataout)
            return HttpResponse(jsonout,content_type="application/json")


        else:
            status_code = 400
            dataout = {'status_code':status_code}
            jsonout = json.dumps(dataout)
            return HttpResponse(jsonout,content_type="application/json")

@csrf_exempt
def hardware(request):
    if(request.method == "GET"):
        if 'userid' in request.GET:
            userid = request.GET['userid']
            hardware = Hardware.objects.filter(user_id=userid)
            hardwareobject = json.loads(serializers.serialize('json',hardware))
            dataout = {'status_code':200,'hardwareobject':hardwareobject}
            jsonout = json.dumps(dataout)
            return HttpResponse(jsonout,content_type='application/json')

        else:
            dataout = 'no user id'
            dataout = json.dumps(dataout)
            return HttpResponse(dataout, content_type="application/json")
    elif(request.method == "POST"):
        datain = request.POST
        userid = datain['userid']
        hardwarename = datain['hardwarename']
        hardwareport = datain['hardwareport']
        hardware = Hardware(user_id=userid,user_hardwarename=hardwarename,user_hardwareport=hardwareport)
        hardware.save()
        status_code = 200
        hardwareobject = json.loads(serializers.serialize('json',hardware))
        dataout = {'status_code':status_code,'hardwareobject':hardwareobject}
        jsonout = json.dumps(dataout)
        return HttpResponse(jsonout,content_type='application/json')


@csrf_exempt
def updatehw(request):
    if (request.method == "POST"):
        datain = request.POST
        userid = datain['userid']
        hardwareid = datain['hardwareid']
        hardwarename = datain['hardwarename']
        hardwareport = datain['hardwareport']
        hardware = Hardware.objects.get(pk=hardwareid)
        if (hardware.user_id == userid):
            hardware.user_hardwarename = hardwarename
            hardware.user_hardwareport = hardwareport
            hardware.save()
            status_code = 200
        else:
            status_code = 400
        dataout = {'status_code': status_code}
        jsonout = json.dumps(dataout)
        return HttpResponse(jsonout, content_type="application/json")

@csrf_exempt
def deletehw(request):
    if(request.method == "POST"):
        datain = request.POST
        userid = datain['userid']
        hardwareid = datain['hardwareid']
        hardware = Hardware.objects.get(pk=hardwareid)
        if(hardware.user_id == userid):
            hardware.delete()
            status_code = 200
        else:
            status_code = 400
        dataout = {'status_code':status_code}
        jsonout = json.dumps(dataout)
        return HttpResponse(jsonout,content_type="application/json")