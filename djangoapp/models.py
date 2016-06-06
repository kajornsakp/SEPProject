from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CustomUser(models.Model):
    user_user = models.OneToOneField(User,default=None);
    user_id = models.CharField(max_length=10,default="0");
    user_type = models.CharField(max_length=10);


class Note(models.Model):
    user_id = models.CharField(max_length=10,default="0");
    user_noteheader = models.CharField(max_length=20,null=True)
    user_note = models.TextField();
    note_date = models.DateField();
    note_time = models.TimeField();

class Reminder(models.Model):
    user_id = models.CharField(max_length=10,default="0");
    user_remindnote = models.CharField(max_length=50);
    user_adddate = models.DateField();
    user_reminddate = models.DateField();
    user_remindtime = models.TimeField();


class Calendar(models.Model):
    user_id = models.CharField(max_length=10,default="0");
    user_event = models.CharField(max_length=50);
    user_date = models.DateField();

class Hardware(models.Model):
    user_id = models.CharField(max_length=10,default="0");
    user_hardwarename = models.CharField(max_length=20)
    user_hardwareport = models.CharField(max_length=20)


class History(models.Model):
    user_id = models.CharField(max_length=10)
    user_querystring = models.TextField()
    user_responsestring = models.TextField()

