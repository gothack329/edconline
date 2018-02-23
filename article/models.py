# coding=utf-8
from django.db import models
from tinymce.models import HTMLField
#from tagging.fields import TagField
#from tagging.models import Tag

# Create your models here.

class Article(models.Model):
    id=models.AutoField(primary_key=True)
    #catalog=models.ForeignKey(Catalogs)
    author = models.CharField(max_length=128,default='小志')
    publish_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=1024)
    detail = HTMLField()
    tag = models.CharField(max_length=128, blank=True, null=True)
    visible = models.CharField(choices=((u'Y',u'是'),(u'N',u'否')),max_length=64,default='N')
    readtime = models.IntegerField(default=0)

    def set_tags(self, tags):
        Tag.objects.update_tags(self, tags)
    def get_tags(self, tags):
        return Tag.objects.get_for_object(self)
    def __unicode__(self):
        return self.title
    class Meta:
        db_table ="articles"
        ordering = ['-publish_date']

