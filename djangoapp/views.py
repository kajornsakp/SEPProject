from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core.context_processors import csrf
# Create your views here.
from djangoapp.models import Person
import json


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
        b = Person.objects.get()
        print(type(b))
        return render(request,'djangoapp/index.html',context)
        strout = ''
        #return HttpResponse("HELLOOOOOOO")
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
        personA = Person.objects.create(first_name="Hi")
        context = {
            'number_list' : number_list,
            'hellostring' : hellostring,
        }
        personA.save()
        context.update(csrf(request))
        #return render(request,'djangoapp/index.html',context)
        return HttpResponse(json.dumps(context),content_type="application/json")