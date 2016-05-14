from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CustomUser(models.Model):
    user = models.ManyToManyField(User)
    user_type = models.CharField(max_length=10)

    def getUserInfo(self):
        return self.user.get_username()+" : "+ self.user.get_full_name()

class CommandLog(models.Model):
    user = models.ManyToManyField(CustomUser)
    command = models.CharField(max_length=100)


class Note(models.Model):
    user = models.ManyToManyField(CustomUser)
    user_note = models.CharField(max_length=50)
    note_date = models.DateField()
    note_time = models.TimeField()
