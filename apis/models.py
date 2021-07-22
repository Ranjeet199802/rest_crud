from django.db import models


# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=200)
    roll_no = models.IntegerField()
    course = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
