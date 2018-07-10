from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    rollno=models.CharField(max_length=10,unique=True)
    first_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=10)
    Mobile_number=models.IntegerField('Mobile_number')
    Address=models.CharField(max_length=20)
    College=models.CharField(max_length=20)
