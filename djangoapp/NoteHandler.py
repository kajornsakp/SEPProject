
from djangoapp.HandlerAbstract import HandlerAbstract
from nltk import word_tokenize
import re,datetime
from django.test import Client


class NoteHandler(HandlerAbstract):

    def __init__(self,userid):
        self.userid = userid
        self.textlist = []

    def handle(self,text):
        textlist = word_tokenize(text)
        noteindex = textlist.index("note")
        self.command = " ".join(textlist[:noteindex])
        self.message = " ".join(textlist[noteindex+1:])
        self.noteheader = textlist[noteindex+1]
        self.date = datetime.datetime.now().date()
        print(self.date)

        self.time = datetime.datetime.now()
        print(self.time)
        c  = Client()
        response = c.post('/note',{'userid':self.userid,'usernote':self.message,'usernoteheader':self.noteheader,'notedate':self.date,'notetime':datetime.datetime.strftime(self.time,"%H:%M:%S")})
        if(response.status_code == 200):
            return "Note was added successfully"
        else:
            return "Failed to added note"