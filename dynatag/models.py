from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from account.models import Profile


# Create your models here.

class Userapp(models.Model):    
    source = models.CharField(max_length=256, null=True)
    Authcontent = models.CharField(max_length=256, null=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    
class Configuration(models.Model):    
    type = models.CharField(max_length=50, null=True)
    initalnum = models.IntegerField(null=True)
    actualnum = models.IntegerField(null=True)
    prefix = models.CharField(max_length=256, null=True)
    suffix = models.CharField(max_length=256, null=True)
    pstartdate = models.DateField(blank=True, null=True)
    penddate = models.DateField(blank=True, null=True)
    targetdate = models.DateField(blank=True, null=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    userapp = models.ForeignKey(Userapp, on_delete=models.CASCADE, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    
class Application(models.Model):
    appname = models.CharField(max_length=256, null=True)
    description = models.CharField(max_length=256, null=True)
    apptoken =  models.CharField(max_length=256, null=True)
    tokenrefresh_time = models.DateTimeField(blank=True, null=True)
    appuri = models.CharField(max_length=256, null=True)
    create_date = models.DateTimeField(blank=True, null=True)