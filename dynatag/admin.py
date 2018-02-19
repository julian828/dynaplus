from django.contrib import admin
from .models import Application, Configuration, Masterdata

# Register your models here.
admin.site.register(Masterdata)
admin.site.register(Application)
admin.site.register(Configuration)
