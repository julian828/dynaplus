from django.db import models
from django.conf import settings
from django.contrib.auth.models import User



# Create your models here.
'''
class Userapp(models.Model):    
    source = models.CharField(max_length=256, null=True)
    Authcontent = models.CharField(max_length=256, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
'''

class Masterdata(models.Model):
    clientid = models.CharField(max_length=256, null=True)
    clientsecret = models.CharField(max_length=256, null=True)
    redirecturl = models.CharField(max_length=256, null=True)
    responsetype = models.CharField(max_length=256, null=True)
    status = models.CharField(max_length=256, null=True)

class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    appname = models.CharField(max_length=256, null=True)
    code = models.CharField(max_length=256, null=True)
    description = models.CharField(max_length=256, null=True)
    accesstoken =  models.CharField(max_length=256, null=True)
    refreshtoken =  models.CharField(max_length=256, null=True)
    tokenrefresh_time = models.DateTimeField(blank=True, null=True)
    appuri = models.CharField(max_length=256, null=True)
    status = models.CharField(max_length=256, null=True)
    create_date = models.DateTimeField(blank=True, null=True)  
    
    def __unicode__(self):
        return self.appname 
     
class Configuration(models.Model):    
    confname = models.CharField(max_length=50, null=True)
    type = models.CharField(max_length=50, null=True)
    initalnum = models.IntegerField(null=True)
    actualnum = models.IntegerField(null=True)
    prefix = models.CharField(max_length=256, null=True)
    suffix = models.CharField(max_length=256, null=True)
    pstartdate = models.DateField(blank=True, null=True)
    penddate = models.DateField(blank=True, null=True)
    targetdate = models.DateField(blank=True, null=True)
    #user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    application = models.ForeignKey(Application, on_delete=models.CASCADE, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    
    def __unicode__(self):
        return self.confname
    

    
    
    
    