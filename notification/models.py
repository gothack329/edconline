from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm,Textarea
from userpage.models import *
from article.models import *

# Create your models here.

class Msg(models.Model):
	id=models.AutoField(primary_key=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    mention_user = models.ManyToManyField(Profile, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    msg_time = models.DateTimeField(auto_now_add=True,editable=False)

    def __str__(self):
        return self.comments


