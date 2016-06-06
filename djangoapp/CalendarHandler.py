
from djangoapp.HandlerAbstract import HandlerAbstract
from nltk import word_tokenize
import re,datetime
from django.test import Client
datenum = {1: "first", 2: "second", 3: "third", 4: "fourth", 5: "fifth",
           6: "six", 7: "seven", 8: "eight",9: "nine",10: "ten",11: "eleven",
           12: "twelve",
           13: "thirteen",
           14: "fourteen",
           15: "fifthteen",
           16: "sixteen",
           17: "seventeen",
           18: "eightteen",
           19: "nineteen",
           20: "twenty",
           21: "twenty one",
           22: "twenty two",
           23: "twenty three",
           24: "twenty four",
           25: "twenty five",
           26: "twenty six",
           27: "twenty seven",
           28: "twenty eight",
           29: "twenty nine",
           30: "thirty",
           31: "thirty one"}
monthnum = {1:"january",2:"february",3:"march",4:"april",5:"may",6:"june",7:"july",8:"august",9:"september",10:"october",11:"november",12:"december"}


class CalendarHandler(HandlerAbstract):

    def __init__(self,userid):
        self.userid = userid
        self.textlist = []


    def handle(self,text):
        textlist = word_tokenize(text)
        eventindex = textlist.index("event")
        onindex = textlist.index("on")
        self.command = " ".join(textlist[:eventindex])
        self.message = " ".join(textlist[eventindex+1:onindex])
        self.date = " ".join(textlist[onindex+1:])
        datetoken = word_tokenize(self.date)
        self.datenumber = ""
        self.monthnumber = ""
        print(datetoken)
        for i in datetoken:
            if i in datenum.values():
                self.datenumber = str(datenum.keys()[datenum.values().index(i)]).zfill(2)

            elif i in monthnum.values():
                self.monthnumber = str(monthnum.keys()[monthnum.values().index(i)]).zfill(2)

        self.yearnumber = str(datetime.datetime.now().year)
        self.datestring = self.yearnumber+'-'+self.monthnumber+"-"+self.datenumber
        self.dateobject = datetime.datetime.strptime(self.datestring,"%Y-%m-%d").date()

        c = Client()
        response = c.post('/calendar',{'userid':self.userid,'userevent':self.message,'userdate':self.dateobject})
        if(response.status_code == 200):
            return "Your calendar event was added successfully"
        else:
            return "Failed to add calendar"

        

