from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
# Create your views here.
from djangoapp.models import Person
import json

@csrf_exempt
def index(request):
        if(request.method == 'GET'):

            number_list = [1,2,3,4,5,6,"hi",999.999]
            hellostring = "GET REQUEST"
            template = loader.get_template('djangoapp/index.html')

            context = {
                'number_list' : number_list,
                'hellostring' : hellostring,
            }
            newjson = json.dumps(context)
            a = Person(first_name="ben",last_name="benn")
            a.save()
            #b = Person.objects.get()
            #print(type(b))
            #return render(request,'djangoapp/index.html',context)
            strout = ''
            return HttpResponse("HELLOOOOOOO")
            #content = request.body['a']
            #print(content  )
            #if(content =='a'):
             #   return HttpResponse("A")
            #else:
            #    return HttpResponse("ELSE")

        elif request.method == 'POST':

            number_list = [1,2,3,4,5,6]
            hellostring = "POST REQUEST"
            template = loader.get_template('djangoapp/index.html')
            person = Person.objects.filter(pk=1)
            data = serializers.serialize("json",person)
            print(data)
            context = {
                'number_list' : number_list,
                'hellostring' : hellostring,
                'person object':json.loads(data),
            }

            #return render(request,'djangoapp/index.html',context)
            return HttpResponse(json.dumps(context),content_type="application/json")

@login_required
def login(username="",password=""):
    print("SECONDINDEX")
    a = Person.objects.get(pk=1)
    print(a)