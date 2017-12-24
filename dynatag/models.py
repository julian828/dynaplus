from django.db import models

# Create your models here.
class User(models.Model):    
    company = models.CharField(max_length=256, null=True)
    address_street = models.CharField(max_length=256, null=True)
    address_city = models.CharField(max_length=256, null=True)
    address_province = models.CharField(max_length=256, null=True)
    address_country = models.CharField(max_length=256, null=True)
    user_regid = models.IntegerField(null=True)
    
    
class Application(models.Model):    
    source = models.CharField(max_length=256, null=True)
    Authcontent = models.CharField(max_length=256, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
class Configuration(models.Model):    
    type = models.CharField(max_length=50, null=True)
    initalnum = models.IntegerField(null=True)
    actualnum = models.IntegerField(null=True)
    prefix = models.CharField(max_length=256, null=True)
    suffix = models.CharField(max_length=256, null=True)
    pstartdate = models.DateField
    penddate = models.DateField
    targetdate = models.DateField
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    application = models.ForeignKey(Application, on_delete=models.CASCADE, null=True)