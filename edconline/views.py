from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext,Template,Context,loader,defaultfilters
from django.shortcuts import render_to_response
from article.models import *
import os,random
import userpage 

# Create your views here.

def user_login(request):
    return {
        'username':request.user,
    }

def homepage(request):

    if request.user.is_authenticated :# and request.user.has_perm('cmdb.permit')):
        username = request.user.username
    else:
        username = None

    imgs = os.listdir('static/upload/')
    cover = random.sample(imgs,1)[0]

    arts = Article.objects.all()
    secs = Section.objects.all()
    return render(request,'index.html',{'cover':cover,'username':username,'arts':arts,'secs':secs}) 


