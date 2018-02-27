from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.db.models import Q
from django.template import Template,Context,loader,defaultfilters
from django.shortcuts import render_to_response
from article.models import *
import os,random
import userpage 
from . import globalarg

# Create your views here.

def homepage(request):
    query = request.GET.items() 
    data = {}
    for i in query:
        data[i[0]]=i[1] 

    if request.user.is_authenticated :# and request.user.has_perm('cmdb.permit')):
        username = request.user.username
    else:
        username = None

    imgs = os.listdir('static/upload/')
    cover = random.sample(imgs,1)[0]

    if 'catalog' in data:
        qset = (Q(section__name=data['catalog']))
        arts = Article.objects.filter(qset).order_by('-publish_time')
    else:
        arts = Article.objects.all().order_by('-publish_time')

    return render(request,'index.html',{'cover':cover,'username':username,'arts':arts},[globalarg.settings]) 


