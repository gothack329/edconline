from django.contrib import admin
from article.models import *

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id','section','title','author','author_id','publish_time','visible')
admin.site.register(Article,ArticleAdmin)


class SectionAdmin(admin.ModelAdmin):
    list_display=('id','name')
admin.site.register(Section,SectionAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display=('id','article','user','mail','ip','comment_time','comment')
admin.site.register(Comment,CommentAdmin)
