from django.db import models
from django import forms

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=70)
    email=models.EmailField(default=' ')
    address=models.CharField(max_length=70,default=' ')
    password=models.CharField(max_length=10)
    re_password=models.CharField(max_length=10)