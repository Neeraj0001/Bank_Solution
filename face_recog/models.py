
# Create your models here.
from django.db import models

from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User,null=True,blank=True, on_delete=models.CASCADE)

    name=models.CharField(null=True,max_length=200)
    Email=models.CharField(null=True,max_length=200)
    Phone=models.CharField(null=True,max_length=200)
    Account_No = models.CharField(null=True,max_length=200)
    Debit_Card_No = models.CharField(null=True,max_length=200)

    Exp_Date = models.DateField(auto_now_add=False,auto_now=False,blank=True,null=True)
    profile_pics=models.ImageField(default="unknown.png",null=True,blank=True)
    # def __str__(self):
    #     return self.user.username
class Bank_Chit(models.Model):
    

    name=models.CharField(null=True,max_length=200)
    Email=models.CharField(null=True,max_length=200)
    Phone=models.CharField(null=True,max_length=200)
    Account_No = models.CharField(null=True,max_length=200)
    Debit_Card_No = models.CharField(null=True,max_length=200)

    Exp_Date = models.DateField(auto_now_add=False,auto_now=False,blank=True,null=True)

