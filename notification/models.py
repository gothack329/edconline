from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm,Textarea
from userpage.models import Profile
from article.models import Comment
from django.db.models.signals import post_save
from django.dispatch import receiver
from bs4 import BeautifulSoup as bs

# Create your models here.

class Msg(models.Model):
    id=models.AutoField(primary_key=True)
    mention_user = models.ManyToManyField(Profile)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    unread = models.CharField(choices=(('Y','是'),('N','否')),max_length=8,default='Y')
    comment_time = models.DateTimeField(auto_now_add=True,editable=False)


@receiver(post_save, sender=Comment)
def mentioned_user(sender, created, instance, **kwargs):
    s = bs(str(instance) , "html.parser")
    mu = [i.text for i in s.find_all('a',attrs={'class':'mentioned_user'})]
    mu = list(set(mu))
    if len(mu) > 0 and created:
        msg = Msg.objects.create(comment=instance,unread='Y',comment_time=instance.comment_time)
        for user in mu:
            inst_u = User.objects.get(username=user)
            inst_p = Profile.objects.get(user=inst_u)
            inst_p.unread += 1
            msg.mention_user.add(inst_p)
            inst_p.save()
        msg.save()

        
