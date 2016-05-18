from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CustomUser(models.Model):
    user = models.ManyToManyField(User)
    user_id = models.CharField(max_length=10,default="0")
    user_type = models.CharField(max_length=10)

    def getUserInfo(self):
        return self.user.get_username()+" : "+ self.user.get_full_name()


class Note(models.Model):
    user_id = models.CharField(max_length=10)
    user_note = models.CharField(max_length=50)
    note_date = models.DateField()
    note_time = models.TimeField()

class Reminder(models.Model):
    user_id = models.CharField(max_length=10)
    user_remindnote = models.CharField(max_length=50)
    user_adddate = models.DateField()
    user_reminddate = models.DateField()
    user_remindtime = models.TimeField()

class Calendar(models.Model):
    user_id = models.CharField(max_length=10)
    user_event = models.CharField(max_length=50)
    user_date = models.DateField()