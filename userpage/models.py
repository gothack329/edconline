from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm,Textarea,TextInput,ClearableFileInput,FileInput
from django.db.models.signals import post_save
from django.dispatch import receiver
#from notification.models import Msg

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    #birth_date = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to='static/avatar/', blank=True, null=True)
    point = models.IntegerField()
    unread = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance,point=10)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


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
