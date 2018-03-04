from django.contrib import admin
from .models import *

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','location','avatar')
admin.site.register(Profile,ProfileAdmin)


class PointAdmin(admin.ModelAdmin):
    list_display = ('user','point_record','record_time','event')
admin.site.register(Point,PointAdmin)
