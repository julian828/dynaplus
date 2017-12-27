from django.contrib import admin
from .models import Profile, Application, Configuration

# Register your models here.
admin.site.register(Profile)
admin.site.register(Application)
admin.site.register(Configuration)
