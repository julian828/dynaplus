from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from account.models import Profile


# Create your models here.

class Application(models.Model):    
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
    application = models.ForeignKey(Application, on_delete=models.CASCADE, null=True)
    create_date = models.DateTimeField(blank=True, null=True)