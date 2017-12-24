from django.contrib import admin
from .models import User, Application, Configuration

# Register your models here.
admin.site.register(User)
admin.site.register(Application)
admin.site.register(Configuration)
