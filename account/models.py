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
    