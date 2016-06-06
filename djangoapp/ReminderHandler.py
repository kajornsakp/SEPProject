from django.test import Client
from djangoapp.HandlerAbstract import HandlerAbstract
from nltk import word_tokenize
import re,datetime


class RemiderHandler(HandlerAbstract):

    def __init__(self,userid):
        self.userid = userid
        self.textlist = []


    def handle(self,text):
        textlist = word_tokenize(text)
        toindex = textlist.index("to")
        onindex = textlist.index("on")
        self.command = " ".join(textlist[:toindex])
        self.message = " ".join(textlist[toindex+1:onindex])
        self.time = " ".join(textlist[onindex+1:])
        self.getdate()

        c = Client()
        response = c.post('/reminder',{"userid":self.userid,"remindnote":self.message,"adddate":datetime.datetime.now().date(),"reminddate":self.date,"remindtime":"08:00:00"})
        if(response.status_code == 200):
            return "Reminder was added already"
        else:
            return "Failed to add reminder"

    def getdate(self):
        if ("today" in self.time):
            self.date = datetime.datetime.now().date()
            self.time.replace("today", "")
        elif ("yesterday" in self.time):
            self.date = datetime.datetime.now().date() - datetime.timedelta(1)
            self.time.replace("yesterday", "")
        elif ("tomorrow" in self.time):
            self.date = datetime.datetime.now().date() + datetime.timedelta(1)
            self.time.replace("tomorrow", "")



