from django.contrib import admin

# Register your models here.
from .models import Users,Topic,Opinion

admin.site.register(Users)
admin.site.register(Topic)
admin.site.register(Opinion)

