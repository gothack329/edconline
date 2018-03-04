from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm,Textarea,TextInput,ClearableFileInput,FileInput
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    #birth_date = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to='static/avatar/', default='static/avatar/default.png', blank=True, null=True)
    point = models.IntegerField(default=0)
    unread = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email')
        widgets = {
            'username':TextInput(attrs={'class':'form-control','placeholder':"Username"}),
            'email':TextInput(attrs={'class':'form-control','placeholder':"E-mail"}),
            'first_name':TextInput(attrs={'class':'form-control','placeholder':"First Name"}),
            'last_name':TextInput(attrs={'class':'form-control','placeholder':"Last Name"}),
           }

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('avatar',)
        error_messages = {
            'avatar':{'required': '请上传头像'},
            }
        widgets = {
           'avatar':ClearableFileInput(attrs={'class':'form-control','placeholder':"头像"}),
            }


class Point(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    point_record = models.IntegerField()
    record_time = models.DateTimeField(auto_now_add=True,editable=False)
    event = models.CharField(choices=(('publish','发布文章'),('comment','发表评论'),('commented','文章被评论'),('register','新用户注册')),max_length=16)

    def __str__(self):
        return '%s %s %d' % (self.user,self.event,self.point_record)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

@receiver(post_save, sender=Point)
def update_user_point(sender, instance, created, **kwargs):
    if created:
        user = Profile.objects.get(user=instance.user)
        user.point += instance.point_record
        user.save()
