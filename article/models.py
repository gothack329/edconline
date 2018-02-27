# coding=utf-8
from django.db import models
from tinymce.models import HTMLField,TinyMCE
from django.contrib.auth.models import User
from django.forms import ModelForm,Textarea
from userpage.models import *
#from django.conf import settings
#from tagging.fields import TagField
#from tagging.models import Tag

# Create your models here.

class Section(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    class Meta:
        db_table ="Section"


class Article(models.Model):
    id=models.AutoField(primary_key=True)
    section=models.ForeignKey(Section,on_delete=models.CASCADE,default=0)
    author_id = models.ForeignKey(Profile,on_delete=models.CASCADE,default=0)
    author = models.CharField(max_length=128,default='')
    #author_id = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    publish_time = models.DateTimeField(auto_now_add=True,editable=False)
    cover = models.ImageField(upload_to='static/upload/', blank=True, null=True)
    title = models.CharField(max_length=1024)
    detail = HTMLField()
    ip = models.GenericIPAddressField(blank=True,null=True)
    tag = models.CharField(max_length=128, blank=True, null=True)
    visible = models.CharField(choices=(('Y','是'),('N','否')),max_length=64,default='N')
    readtime = models.IntegerField(default=0)

    #def set_tags(self, tags):
    #    Tag.objects.update_tags(self, tags)
    #def get_tags(self, tags):
    #    return Tag.objects.get_for_object(self)
    def __str__(self):
        return self.title

    class Meta:
        db_table ="article"
        ordering = ['-publish_time']

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title','author','section','tag','cover','detail']
        widgets = {
                    'detail':TinyMCE(attrs={'cols':'100%','rows':50}),
                }


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    article = models.ForeignKey(Article,on_delete=models.CASCADE,default=0)
    user = models.ForeignKey(Profile,on_delete=models.CASCADE,default=0) 
    comment_time = models.DateTimeField(auto_now_add=True,editable=False)
    comment = HTMLField()
    ip = models.GenericIPAddressField()
    clickcount = models.IntegerField(default=0)
    refer = models.CharField(max_length=5096,default='none')
    agent = models.CharField(max_length=5096,default='none')

    def __str__(self):
        return self.comment
        #return '用户%s发表留言。' % {self.uname}
    class Meta:
        db_table ="comment"
        ordering = ['-comment_time']

class CommentForm(ModelForm):
    class Meta:
        model = Comment 
        fields = ('article','user','comment','ip')
        widgets = {
                'comment':TinyMCE(attrs={'cols':'100%','rows':10}),
                }
