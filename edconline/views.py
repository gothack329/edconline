from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.db.models import Q
from django.template import Template,defaultfilters,RequestContext
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

    #if request.user.is_authenticated :# and request.user.has_perm('cmdb.permit')):
    #    username = request.user.username
    #else:
    #    username = None

    imgs = os.listdir('static/upload/')
    cover = random.sample(imgs,1)[0]


    if 'catalog' in data:
        qset = (Q(section__name=data['catalog']))
        arts = Article.objects.filter(qset).filter(visible='Y').order_by('-publish_time')
        search_keywords = data['catalog']
    elif 'keywords' in data:
        qset = (Q(title__icontains = data['keywords'])|Q(detail__icontains = data['keywords']))
        arts = Article.objects.filter(qset).filter(visible='Y').order_by('-publish_time')
        search_keywords = data['keywords']
    else:
        arts = Article.objects.filter(visible='Y').order_by('-publish_time')
        search_keywords = None

    return render(request,'index.html',{'cover':cover,'arts':arts,'keywords':search_keywords}) 









