# coding=utf-8
from django.db import models
from tinymce.models import HTMLField,TinyMCE
from django.contrib.auth.models import User
from django.forms import *
from userpage.models import *
from django.db.models.signals import post_save
from django.dispatch import receiver
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
    comment_count = models.IntegerField(default=0)
    #update_time = models.DateTimeField(auto_now=True,blank=True,null=True)

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
        fields = ['title','author','author_id','section','tag','cover','detail']
        error_messages = {
            'section':{'required': '请选择主题分区'},
            'author':{'required': '请输入作者名称'},
            'cover':{'required': '请上传封面图'},
            'detail':{'required': '请输入正文内容'},
            'title':{'required': '请输入文章标题'},

            }
        widgets = {
           'detail':TinyMCE(attrs={'cols':'100%','rows':30}),
           'cover':ClearableFileInput(attrs={'style':'width:50%','class':'form-control','placeholder':"封面"}),
           'tag':TextInput(attrs={'class':'form-control','placeholder':"添加标签,回车确认",'data-role':'tagsinput'}),
           'author':TextInput(attrs={'class':'form-control','placeholder':"署名"}),
           'title':TextInput(attrs={'style':'width:50%','class':'form-control','placeholder':"标题"}),
           'section':widgets.Select(choices=Section.objects.values_list('id','name'),attrs={'class':'form-control','placeholder':"标题"}), 
            }


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    article = models.ForeignKey(Article,on_delete=models.CASCADE,default=0)
    user = models.ForeignKey(Profile,on_delete=models.CASCADE,default=0) 
    comment_time = models.DateTimeField(auto_now_add=True,editable=False)
    comment = HTMLField()
    invalid = models.CharField(choices=(('Y','是'),('N','否')),max_length=64,default='N')
    ip = models.GenericIPAddressField(blank=True,null=True,default='0.0.0.0')
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
        fields = ('article','user','comment','ip','invalid')
        widgets = {
                'comment':TinyMCE(attrs={'cols':'100%','rows':10}),
                }


@receiver(post_save, sender=Comment)
def comment_count(sender, created, instance, **kwargs):
    if created:
        art = Article.objects.get(pk=instance.article.id)
        art.comment_count += 1
        art.save()
