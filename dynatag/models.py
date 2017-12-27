from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=256, null=True)
    address_street = models.CharField(max_length=256, null=True)
    address_city = models.CharField(max_length=256, null=True)
    address_province = models.CharField(max_length=256, null=True)
    address_country = models.CharField(max_length=256, null=True)
    birthday = models.DateField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    
    def __unicode__(self):
        return self.user.username
    
    
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