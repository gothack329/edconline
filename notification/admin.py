from django.contrib import admin
from .models import *


class MsgAdmin(admin.ModelAdmin):
    list_display=('id','comment_time','unread','comment',)
admin.site.register(Msg,MsgAdmin)
