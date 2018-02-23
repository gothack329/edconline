from django.contrib import admin
from article.models import *

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id','title','author','publish_date','visible')

admin.site.register(Article,ArticleAdmin)
