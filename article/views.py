from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext,Template,Context,loader,defaultfilters
from django.shortcuts import render_to_response

# Create your views here.

def homepage(request):
    return render(request,'base.html') 


def detail(request, article_id):
    return HttpResponse("You're looking at article %s." % article_id)

def vote(request, article_id):
    return HttpResponse("You're voting on article %s." % article_id)
