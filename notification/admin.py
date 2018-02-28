from django.contrib import admin
from .models import *


class MsgAdmin(admin.ModelAdmin):
    list_display=('id','user','mention_user','msg_time')
admin.site.register(Msg,MsgAdmin)
