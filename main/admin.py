from django.contrib import admin

# Register your models here.
from .models import Users,Topic

admin.site.register(Users)
admin.site.register(Topic)

