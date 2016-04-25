from django.db import models
from django.core import serializers
# Create your models here.

class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=20)
    user_password = models.CharField(max_length=20)
    user_type = models.CharField(max_length=20)



class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name + " " + self.last_name


class CommandLog(models.Model):
    user = models.ManyToManyField(User)
    command = models.CharField(max_length=100)


class Note(models.Model):
    user = models.ManyToManyField(User)
    user_note = models.CharField(max_length=50)
    note_date = models.DateField()
    note_time = models.TimeField()
