
from djangoapp.ReminderHandler import RemiderHandler
from djangoapp.CalendarHandler import CalendarHandler
from djangoapp.NoteHandler import NoteHandler
import re
class QueryHandler:

    def __init__(self,userid):
        self.userid = userid
    def classify(self,text):
        if(bool(re.search(r'((\bremind\b.*\bto\b))',text))):
            reminder = RemiderHandler(self.userid)
            return reminder.handle(text)
        elif(bool(re.search(r'((\bevent\b.*\bon\b))',text))):
            calendar = CalendarHandler(self.userid)
            return calendar.handle(text)
        elif(bool(re.search(r'(\bnote\b)',text))):
            note = NoteHandler(self.userid)
            return note.handle(text)
        elif(bool(re.search(r'(\bhi\b)|(\bhello\b)|(\bgreeting\b)',text))):
            return "Hello from ELLE!"
        else:
            return "I don't understand your query"

